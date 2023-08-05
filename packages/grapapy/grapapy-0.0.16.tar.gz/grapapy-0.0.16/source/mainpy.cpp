#include <pybind11/pybind11.h>
#include "pybind11/include/pybind11/pybind11.h"
#include "pybind11/include/pybind11/eval.h"

namespace py = pybind11;

#define STRINGIFY(x) #x
#define MACRO_STRINGIFY(x) STRINGIFY(x)

#include <iostream>
#include <string>

#include "grapa/GrapaLink.h"
#include "grapa/GrapaValue.h"
#include "grapa/GrapaSystem.h"
#include "grapa/GrapaCompress.h"
#include "grapa/GrapaLibRule.h"
#include "grapa/GrapaFloat.h"

#define gGrapaUseWidget false

extern bool gGrapaWidgetMainThread;

class GrapaMainResponse : public GrapaConsoleResponse
{
public:
    virtual void SendCommand(GrapaScriptExec* vScriptExec, GrapaNames* pNameSpace, const void* sendbuf, u64 sendbuflen)
    {
    };
    virtual void SendPrompt(GrapaScriptExec* vScriptExec, GrapaNames* pNameSpace, const GrapaBYTE& sendbuf)
    {
    };
    virtual void SendEnd(GrapaScriptExec* vScriptExec, GrapaNames* pNameSpace, GrapaRuleEvent* pValue)
    {
    };
};

class GrapaPyObject
{
public:
	static GrapaRuleEvent* ToGrapa(PyObject* o, GrapaCHAR pname)
	{
		GrapaRuleEvent* result = NULL;
		GrapaCHAR pStr;
		if (PyBool_Check(o))
		{
			long retvalue = PyLong_AsLong(o);
			if (retvalue) pStr.FROM("\1");
			else pStr.FROM("\0");
			pStr.mToken = GrapaTokenType::BOOL;
			result = new GrapaRuleEvent(0, pname, pStr);
		}
		else if (Py_None==o)
		{
			result = new GrapaRuleEvent(0, pname, pStr);
			result->SetNull();
		}
		else if (PyBytes_Check(o))
		{
			const char* buffer = PyBytes_AS_STRING(o);
			Py_ssize_t length = PyBytes_GET_SIZE(o);
			pStr.FROM(buffer, length);
			pStr.mToken = GrapaTokenType::RAW;
			result = new GrapaRuleEvent(0, pname, pStr);
		}
		else if (PyUnicode_Check(o))
		{
			Py_ssize_t size=0;
			char* ptr = (char*)PyUnicode_AsUTF8AndSize(o, &size);
			result = new GrapaRuleEvent(0, pname, GrapaCHAR(ptr, size));
		}
		else if (PyLong_Check(o))
		{
			long long retvalue = PyLong_AsLongLong(o);
			pStr = GrapaInt(retvalue).getBytes();
			result = new GrapaRuleEvent(0, pname, pStr);
		}
		else if (PyFloat_Check(o))
		{
			double retvalue = PyFloat_AS_DOUBLE(o);
			pStr = GrapaFloat(retvalue).getBytes();
			result = new GrapaRuleEvent(0, pname, pStr);
		}
		else if (PyTuple_Check(o))
		{
			result = new GrapaRuleEvent(0, pname, GrapaCHAR());
			result->vQueue = new GrapaRuleQueue();
			result->mValue.mToken = GrapaTokenType::TUPLE;
			for (int i = 0; i < PyTuple_Size(o); ++i)
			{
				PyObject* item = PyTuple_GetItem(o, i);
				result->vQueue->PushTail(ToGrapa(item, GrapaCHAR()));
			}
		}
		else if (PyList_Check(o))
		{
			result = new GrapaRuleEvent(0, pname, GrapaCHAR());
			result->vQueue = new GrapaRuleQueue();
			result->mValue.mToken = GrapaTokenType::ARRAY;
			for (int i = 0; i < PyList_Size(o); ++i)
			{
				PyObject* item = PyList_GetItem(o, i);
				result->vQueue->PushTail(ToGrapa(item, GrapaCHAR()));
			}
		}
		else if (PyDict_Check(o))
		{
			result = new GrapaRuleEvent(0, pname, GrapaCHAR());
			result->vQueue = new GrapaRuleQueue();
			result->mValue.mToken = GrapaTokenType::LIST;
			PyObject* key, * item;
			Py_ssize_t pos = 0;
			while (PyDict_Next(o, &pos, &key, &item))
			{
				Py_ssize_t nsize;
				char* nptr = (char*)PyUnicode_AsUTF8AndSize(key, &nsize);
				GrapaCHAR kname(nptr, nsize);
				result->vQueue->PushTail(ToGrapa(item, kname));
			}
		}
		else
		{
			result = new GrapaRuleEvent(0, pname, GrapaCHAR());
			result->SetNull();
		}
		return result;
	}
	
	static void FromGrapa(GrapaRuleEvent* e, py::object* o)
	{
		if (e == NULL)
		{
			*o = py::none();
			return;
		}
		GrapaInt a;
		GrapaFloat f;
		GrapaCHAR s;
		bool isTrueA = false;
		bool isNegA = false;
		bool isNull = false;
		Py_ssize_t pos = 0;
		switch (e->mValue.mToken)
		{
		case GrapaTokenType::STR:
		case GrapaTokenType::SYSSTR:
			*o = py::str((char*)e->mValue.mBytes, e->mValue.mLength);
			break;
		case GrapaTokenType::INT:
		case GrapaTokenType::SYSINT:
			a.FromBytes(e->mValue);
			*o = py::int_(a.LongValue());
			break;
		case GrapaTokenType::ID:
		case GrapaTokenType::SYSID:
			if (e->IsNull())
				*o = py::none();
			else
				*o = py::str((char*)e->mValue.mBytes, e->mValue.mLength);
			break;
		case GrapaTokenType::RAW:
			*o = py::bytes((char*)e->mValue.mBytes, e->mValue.mLength);
			break;
		case GrapaTokenType::FLOAT:
			f.FromBytes(e->mValue);
			s = f.ToString();
			*o = py::float_(std::stod((char*)s.mBytes));
			break;
		case GrapaTokenType::BOOL:
			if (e) isTrueA = !e->IsNullIsNegIsZero(isNegA, isNull);	
			*o = py::bool_(isTrueA);
			break;
		case GrapaTokenType::ARRAY:
			*o = py::list();
			e = e->vQueue->Head();
			while (e)
			{
				GrapaRuleEvent* e2 = e;
				while (e2 && e2->mValue.mToken == GrapaTokenType::PTR) e2 = e2->vRulePointer;
				py::object o2;
				FromGrapa(e2, &o2);
				((py::list*)o)->append(o2);
				e = e->Next();
			}
			break;
		case GrapaTokenType::TUPLE:
			*o = py::tuple(e->vQueue->mCount);
			e = e->vQueue->Head();
			while (e)
			{
				GrapaRuleEvent* e2 = e;
				while (e2 && e2->mValue.mToken == GrapaTokenType::PTR) e2 = e2->vRulePointer;
				py::object o2;
				FromGrapa(e2, &o2);
				PyTuple_SET_ITEM(o->ptr(), pos, o2.ptr());
				o2.inc_ref();
				pos++;
				e = e->Next();
			}
			break;
		case GrapaTokenType::LIST:
			*o = py::dict();
			e = e->vQueue->Head();
			while (e)
			{
				GrapaRuleEvent* e2 = e;
				while (e2 && e2->mValue.mToken == GrapaTokenType::PTR) e2 = e2->vRulePointer;
				py::object o2;
				FromGrapa(e2, &o2);
				py::str nm((char*)e2->mName.mBytes, e2->mName.mLength);
				PyDict_SetItem(o->ptr(), nm.ptr(), o2.ptr());
				e = e->Next();
			}
			break;
		default:
			*o = py::none();
			break;
		}
	}
};

class GrapaLibraryRulePyEvalEvent : public GrapaLibraryEvent
{
public:
	GrapaLibraryRulePyEvalEvent(GrapaCHAR& pName) { mName.FROM(pName); };
	virtual GrapaRuleEvent* Run(GrapaScriptExec* vScriptExec, GrapaNames* pNameSpace, GrapaRuleEvent* pOperation, GrapaRuleQueue* pInput)
	{
		pybind11::gil_scoped_acquire acquire;
		GrapaRuleEvent* result = NULL;
		GrapaLibraryParam script_param(vScriptExec, pNameSpace, pInput ? pInput->Head(0) : NULL);
		GrapaLibraryParam import_param(vScriptExec, pNameSpace, pInput ? pInput->Head(1) : NULL);
		GrapaLibraryParam attr_param(vScriptExec, pNameSpace, pInput ? pInput->Head(2) : NULL);
		if (script_param.vVal && script_param.vVal->mValue.mLength)
		{
			std::string sript_str;
			GrapaCHAR type_str(""), import_str("__main__"), attr_str("__dict__");
			sript_str.assign((char*)script_param.vVal->mValue.mBytes, script_param.vVal->mValue.mLength);
			if (import_param.vVal && import_param.vVal->mValue.mLength) import_str.FROM(import_param.vVal->mValue);
			if (attr_param.vVal && attr_param.vVal->mValue.mLength) attr_str.FROM(attr_param.vVal->mValue);
			py::object scope = py::module_::import((char*)import_str.mBytes).attr((char*)attr_str.mBytes);
			GrapaCHAR pStr;
			py::object o = py::eval(sript_str, scope);
			result = GrapaPyObject::ToGrapa(o.ptr(), GrapaCHAR());
		}
		return result;
	}
};

class GrapaPyRuleEvent : public GrapaLibraryRuleEvent
{
public:
	GrapaPyRuleEvent(GrapaCHAR pName) { mName.FROM(pName); };
	virtual GrapaLibraryEvent* LoadLib(GrapaScriptExec* vScriptExec, GrapaRuleEvent* pLib, GrapaCHAR& pName)
	{
		GrapaLibraryEvent* lib = NULL;
		if (pName.Cmp("eval") == 0) lib = new GrapaLibraryRulePyEvalEvent(pName);
		return(lib);
	}
};

template <typename... Args>
using overload_cast_ = pybind11::detail::overload_cast_impl<Args...>;

/* https://pybind11.readthedocs.io/en/stable/classes.html
py::class_<Pet>(m, "Pet")
    .def("set", overload_cast_<int>()(&Pet::set), "Set the pet's age")
    .def("set", overload_cast_<const std::string &>()(&Pet::set), "Set the pet's name");
*/

class  GrapaStruct 
{
public:
    GrapaScriptExec mScriptExec;
    GrapaConsoleSend mConsoleSend;
    GrapaMainResponse mConsoleResponse;
    GrapaNames mRuleVariables;
	GrapaStruct()
	{
		mConsoleSend.mScriptState.vScriptExec = &mScriptExec;
		mScriptExec.vScriptState = &mConsoleSend.mScriptState;
		mConsoleSend.mScriptState.SetNameSpace(&mRuleVariables);
		mRuleVariables.SetResponse(&mConsoleResponse);
		mConsoleSend.Start();
		GrapaCHAR grresult;
		GrapaSystem* gSystem = GrapaLink::GetGrapaSystem();
		if (gSystem->mGrammar.mLength)
			grresult = mConsoleSend.SendSync(gSystem->mGrammar, NULL, 0, GrapaCHAR());
		GrapaCHAR runStr("$global[\"$py\"] = class {eval = op(script,import=\"\",attr=\"\"){@<py,eval,{@<var,{script}>,@<var,{import}>,@<var,{attr}>}>();};};");
		grresult = mConsoleSend.SendSync(runStr,NULL,0,GrapaCHAR());
	}
    ~GrapaStruct() 
	{ 
		mConsoleSend.Stop();
	}
	
	void setARG(GrapaCHAR& pStr)
	{
		GrapaRuleEvent* e = mRuleVariables.GetNameQueue()->Tail();
		s64 idx = 0;
		GrapaRuleEvent* v = e->vQueue->Search("$ARG", idx);
		if (v)
		{
			v->CLEAR();
			v->mValue.FROM(pStr);
		}
		else
		{
			mConsoleSend.mScriptState.AddRawParameter(e, GrapaCHAR("$ARG"), pStr);
		}
	}

	void setARG(std::string paramstr)
	{
		GrapaCHAR pStr(paramstr.c_str(), paramstr.length());
		setARG(pStr);
	}

	void setARG(py::object o)
	{
		GrapaRuleEvent* e = GrapaPyObject::ToGrapa(o.ptr(), GrapaCHAR("$ARG"));
		GrapaRuleEvent* q = mRuleVariables.GetNameQueue()->Tail();
		s64 idx = 0;
		GrapaRuleEvent* v = q->vQueue->Search("$ARG", idx);
		if (v)
		{
			q->vQueue->PopEvent(v);
			v->CLEAR();
			delete v;
		}
		GrapaRuleEvent* op = q;
		while (op->mValue.mToken == GrapaTokenType::PTR && op->vRulePointer) op = op->vRulePointer;
		op->vQueue->PushTail(e);
	}

	void setARG(py::bytes parambytes)
	{
		py::buffer_info info(py::buffer(parambytes).request());
		const char* buffer = reinterpret_cast<const char*>(info.ptr);
		size_t length = static_cast<size_t>(info.size);
		GrapaCHAR pStr(buffer, length);
		pStr.mToken = GrapaTokenType::RAW;
		setARG(pStr);
	}

	py::object eval(py::object cmdstr, py::object paramstr, std::string rulestr, std::string profilestr)
	{
		size_t length = 0;
		GrapaCHAR runStr;
		GrapaRuleEvent* rulexx = NULL;
		GrapaCHAR profStr;
		py::object o;
		GrapaRuleEvent* grresult = NULL;
		if (true)
		{
			pybind11::gil_scoped_acquire acquire;
			o = py::none();
			if (PyUnicode_Check(cmdstr.ptr()))
			{
				Py_ssize_t size = 0;
				const char* buffer = (char*)PyUnicode_AsUTF8AndSize(cmdstr.ptr(), &size);
				length = size;
				if (length > 0)
				{
					setARG(paramstr);
					runStr.FROM(buffer, length);
				}
			}
			else if (PyBytes_Check(cmdstr.ptr()))
			{
				const char* buffer = PyBytes_AS_STRING(cmdstr.ptr());
				length = PyBytes_GET_SIZE(cmdstr.ptr());
				if (length > 0)
				{
					setARG(paramstr);
					runStr.FROM(buffer, length);
					runStr.mToken = GrapaTokenType::RAW;
				}
			}
			if (rulestr.length() > 0)
			{
				GrapaCHAR rStr(rulestr.c_str(), rulestr.length());
				rulexx = mConsoleSend.mScriptState.SearchVariable(mConsoleSend.mScriptState.GetNameSpace(), rStr);
			}
			profStr.FROM(profilestr.c_str(), profilestr.length());
		}
		if (length > 0)
		{
			grresult = mConsoleSend.SendSyncResult(runStr, rulexx, 0, profStr);
		}
		if (grresult)
		{
			pybind11::gil_scoped_acquire acquire;
			GrapaRuleEvent* echo = grresult;
			while (echo && echo->mValue.mToken == GrapaTokenType::PTR)
				echo = echo->vRulePointer;
			GrapaPyObject::FromGrapa(echo,&o);
			grresult->CLEAR();
			delete grresult;
		}
		return o;
	}

};

py::object grapa_eval(py::object cmdstr, py::object paramstr, std::string rulestr, std::string profilestr)
{
	GrapaStruct gs;
	return gs.eval(cmdstr,paramstr,rulestr,profilestr);
}

PYBIND11_MODULE(grapapy, m)
{
	GrapaCHAR inStr, outStr, runStr;
	bool needExit = false, showConsole = false, showWidget = false;
	GrapaCHAR s = GrapaLink::Start(needExit, showConsole, showWidget, inStr, outStr, runStr);
	GrapaLink::GetGrapaSystem()->mLibraryQueue.PushTail(new GrapaPyRuleEvent(GrapaCHAR("py")));

    m.doc() = R"pbdoc(
        GrapaPy extention
        -----------------------

        .. currentmodule:: grapapy

        .. autosummary::
           :toctree: _generate

           new - create an instance (state maintained between calls)
		   eval - eval a string, return a string

		   Pass in 2'nd parameter as string or bytes, available using @$ARG in the script. 
		   
    )pbdoc";

	py::class_<GrapaStruct>(m, "grapa")
		.def(py::init<>())
		.def("eval", static_cast<py::object(GrapaStruct::*)(py::object, py::object, std::string, std::string)>(&GrapaStruct::eval), "", py::arg("s"), py::arg("a") = "", py::arg("r") = "", py::arg("p") = "", pybind11::call_guard<py::gil_scoped_release>())
		;
	
	m.def("eval", &grapa_eval, R"pbdoc(
        Evaluate a Grapa script
    )pbdoc",
		py::arg("s"), py::arg("a") = "", py::arg("r") = "", py::arg("p") = "", pybind11::call_guard<py::gil_scoped_release>());
	
    m.attr("__version__") = "0.0.16";
	
	// GrapaLink::Stop();
}
