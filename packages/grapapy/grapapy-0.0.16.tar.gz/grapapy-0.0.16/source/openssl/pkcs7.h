/*
 * Copyright 1995-2016 The OpenSSL Project Authors. All Rights Reserved.
 *
 * Licensed under the OpenSSL license (the "License").  You may not use
 * this file except in compliance with the License.  You can obtain a copy
 * in the file LICENSE in the source distribution or at
 * https://www.openssl.org/source/license.html
 */

#ifndef HEADER_PKCS7_H
# define HEADER_PKCS7_H

# include <openssl/asn1.h>
# include <openssl/bio.h>
# include <openssl/e_os2.h>

# include <openssl/symhacks.h>
# include <openssl/ossl_typ.h>
# include <openssl/pkcs7err.h>

#ifdef  __cplusplus
extern "C" {
#endif

/*-
Encryption_ID           DES-CBC
Digest_ID               MD5
Digest_Encryption_ID    rsaEncryption
Key_Encryption_ID       rsaEncryption
*/

typedef struct pkcs7_issuer_and_serial_st {
    X509_NAME *issuer;
    ASN1_INTEGER *serial;
} PKCS7_ISSUER_AND_SERIAL;

typedef struct pkcs7_signer_info_st {
    ASN1_INTEGER *version;      /* version 1 */
    PKCS7_ISSUER_AND_SERIAL *issuer_and_serial;
    X509_ALGOR *digest_alg;
    STACK_OF(X509_ATTRIBUTE) *auth_attr; /* [ 0 ] */
    X509_ALGOR *digest_enc_alg;
    ASN1_OCTET_STRING *enc_digest;
    STACK_OF(X509_ATTRIBUTE) *unauth_attr; /* [ 1 ] */
    /* The private key to sign with */
    EVP_PKEY *pkey;
} PKCS7_SIGNER_INFO;

DEFINE_STACK_OF(PKCS7_SIGNER_INFO)

typedef struct pkcs7_recip_info_st {
    ASN1_INTEGER *version;      /* version 0 */
    PKCS7_ISSUER_AND_SERIAL *issuer_and_serial;
    X509_ALGOR *key_enc_algor;
    ASN1_OCTET_STRING *enc_key;
    X509 *cert;                 /* get the pub-key from this */
} PKCS7_RECIP_INFO;

DEFINE_STACK_OF(PKCS7_RECIP_INFO)

typedef struct pkcs7_signed_st {
    ASN1_INTEGER *version;      /* version 1 */
    STACK_OF(X509_ALGOR) *md_algs; /* md used */
    STACK_OF(X509) *cert;       /* [ 0 ] */
    STACK_OF(X509_CRL) *crl;    /* [ 1 ] */
    STACK_OF(PKCS7_SIGNER_INFO) *signer_info;
    struct pkcs7_st *contents;
} PKCS7_SIGNED;
/*
 * The above structure is very very similar to PKCS7_SIGN_ENVELOPE. How about
 * merging the two
 */

typedef struct pkcs7_enc_content_st {
    ASN1_OBJECT *content_type;
    X509_ALGOR *algorithm;
    ASN1_OCTET_STRING *enc_data; /* [ 0 ] */
    const EVP_CIPHER *cipher;
} PKCS7_ENC_CONTENT;

typedef struct pkcs7_enveloped_st {
    ASN1_INTEGER *version;      /* version 0 */
    STACK_OF(PKCS7_RECIP_INFO) *recipientinfo;
    PKCS7_ENC_CONTENT *enc_data;
} PKCS7_ENVELOPE;

typedef struct pkcs7_signedandenveloped_st {
    ASN1_INTEGER *version;      /* version 1 */
    STACK_OF(X509_ALGOR) *md_algs; /* md used */
    STACK_OF(X509) *cert;       /* [ 0 ] */
    STACK_OF(X509_CRL) *crl;    /* [ 1 ] */
    STACK_OF(PKCS7_SIGNER_INFO) *signer_info;
    PKCS7_ENC_CONTENT *enc_data;
    STACK_OF(PKCS7_RECIP_INFO) *recipientinfo;
} PKCS7_SIGN_ENVELOPE;

typedef struct pkcs7_digest_st {
    ASN1_INTEGER *version;      /* version 0 */
    X509_ALGOR *md;             /* md used */
    struct pkcs7_st *contents;
    ASN1_OCTET_STRING *digest;
} PKCS7_DIGEST;

typedef struct pkcs7_encrypted_st {
    ASN1_INTEGER *version;      /* version 0 */
    PKCS7_ENC_CONTENT *enc_data;
} PKCS7_ENCRYPT;

typedef struct pkcs7_st {
    /*
     * The following is non NULL if it contains ASN1 encoding of this
     * structure
     */
    unsigned char *asn1;
    long length;
# define PKCS7_S_HEADER  0
# define PKCS7_S_BODY    1
# define PKCS7_S_TAIL    2
    int state;                  /* used during processing */
    int detached;
    ASN1_OBJECT *type;
    /* content as defined by the type */
    /*
     * all encryption/message digests are applied to the 'contents', leaving
     * out the 'type' field.
     */
    union {
        char *ptr;
        /* NID_pkcs7_data */
        ASN1_OCTET_STRING *data;
        /* NID_pkcs7_signed */
        PKCS7_SIGNED *sign;
        /* NID_pkcs7_enveloped */
        PKCS7_ENVELOPE *enveloped;
        /* NID_pkcs7_signedAndEnveloped */
        PKCS7_SIGN_ENVELOPE *signed_and_enveloped;
        /* NID_pkcs7_digest */
        PKCS7_DIGEST *digest;
        /* NID_pkcs7_encrypted */
        PKCS7_ENCRYPT *encrypted;
        /* Anything else */
        ASN1_TYPE *other;
    } d;
} PKCS7;

DEFINE_STACK_OF(PKCS7)

# define PKCS7_OP_SET_DETACHED_SIGNATURE 1
# define PKCS7_OP_GET_DETACHED_SIGNATURE 2

# define PKCS7_get_signed_attributes(si) ((si)->auth_attr)
# define PKCS7_get_attributes(si)        ((si)->unauth_attr)

# define PKCS7_type_is_signed(a) (OBJ_obj2nid((a)->type) == NID_pkcs7_signed)
# define PKCS7_type_is_encrypted(a) (OBJ_obj2nid((a)->type) == NID_pkcs7_encrypted)
# define PKCS7_type_is_enveloped(a) (OBJ_obj2nid((a)->type) == NID_pkcs7_enveloped)
# define PKCS7_type_is_signedAndEnveloped(a) \
                (OBJ_obj2nid((a)->type) == NID_pkcs7_signedAndEnveloped)
# define PKCS7_type_is_data(a)   (OBJ_obj2nid((a)->type) == NID_pkcs7_data)
# define PKCS7_type_is_digest(a)   (OBJ_obj2nid((a)->type) == NID_pkcs7_digest)

# define PKCS7_set_detached(p,v) \
                PKCS7_ctrl(p,PKCS7_OP_SET_DETACHED_SIGNATURE,v,NULL)
# define PKCS7_get_detached(p) \
                PKCS7_ctrl(p,PKCS7_OP_GET_DETACHED_SIGNATURE,0,NULL)

# define PKCS7_is_detached(p7) (PKCS7_type_is_signed(p7) && PKCS7_get_detached(p7))

/* S/MIME related flags */

# define PKCS7_TEXT              0x1
# define PKCS7_NOCERTS           0x2
# define PKCS7_NOSIGS            0x4
# define PKCS7_NOCHAIN           0x8
# define PKCS7_NOINTERN          0x10
# define PKCS7_NOVERIFY          0x20
# define PKCS7_DETACHED          0x40
# define PKCS7_BINARY            0x80
# define PKCS7_NOATTR            0x100
# define PKCS7_NOSMIMECAP        0x200
# define PKCS7_NOOLDMIMETYPE     0x400
# define PKCS7_CRLFEOL           0x800
# define PKCS7_STREAM            0x1000
# define PKCS7_NOCRL             0x2000
# define PKCS7_PARTIAL           0x4000
# define PKCS7_REUSE_DIGEST      0x8000
# define PKCS7_NO_DUAL_CONTENT   0x10000

/* Flags: for compatibility with older code */

# define SMIME_TEXT      PKCS7_TEXT
# define SMIME_NOCERTS   PKCS7_NOCERTS
# define SMIME_NOSIGS    PKCS7_NOSIGS
# define SMIME_NOCHAIN   PKCS7_NOCHAIN
# define SMIME_NOINTERN  PKCS7_NOINTERN
# define SMIME_NOVERIFY  PKCS7_NOVERIFY
# define SMIME_DETACHED  PKCS7_DETACHED
# define SMIME_BINARY    PKCS7_BINARY
# define SMIME_NOATTR    PKCS7_NOATTR

/* CRLF ASCII canonicalisation */
# define SMIME_ASCIICRLF         0x80000

DECLARE_ASN1_FUNCTIONS(PKCS7_ISSUER_AND_SERIAL)

int PKCS7_ISSUER_AND_SERIAL_digest(PKCS7_ISSUER_AND_SERIAL *data,
                                   const EVP_MD *type, unsigned char *md,
                                   unsigned int *len);
# ifndef OPENSSL_NO_STDIO
PKCS7 *d2i_PKCS7_fp(FILE *fp, PKCS7 **p7);
int i2d_PKCS7_fp(FILE *fp, PKCS7 *p7);
# endif
PKCS7 *PKCS7_dup(PKCS7 *p7);
PKCS7 *d2i_PKCS7_bio(BIO *bp, PKCS7 **p7);
int i2d_PKCS7_bio(BIO *bp, PKCS7 *p7);
int i2d_PKCS7_bio_stream(BIO *out, PKCS7 *p7, BIO *in, int flags);
int PEM_write_bio_PKCS7_stream(BIO *out, PKCS7 *p7, BIO *in, int flags);

DECLARE_ASN1_FUNCTIONS(PKCS7_SIGNER_INFO)
DECLARE_ASN1_FUNCTIONS(PKCS7_RECIP_INFO)
DECLARE_ASN1_FUNCTIONS(PKCS7_SIGNED)
DECLARE_ASN1_FUNCTIONS(PKCS7_ENC_CONTENT)
DECLARE_ASN1_FUNCTIONS(PKCS7_ENVELOPE)
DECLARE_ASN1_FUNCTIONS(PKCS7_SIGN_ENVELOPE)
DECLARE_ASN1_FUNCTIONS(PKCS7_DIGEST)
DECLARE_ASN1_FUNCTIONS(PKCS7_ENCRYPT)
DECLARE_ASN1_FUNCTIONS(PKCS7)

DECLARE_ASN1_ITEM(PKCS7_ATTR_SIGN)
DECLARE_ASN1_ITEM(PKCS7_ATTR_VERIFY)

DECLARE_ASN1_NDEF_FUNCTION(PKCS7)
DECLARE_ASN1_PRINT_FUNCTION(PKCS7)

long PKCS7_ctrl(PKCS7 *p7, int cmd, long larg, char *parg);

int PKCS7_set_type(PKCS7 *p7, int type);
int PKCS7_set0_type_other(PKCS7 *p7, int type, ASN1_TYPE *other);
int PKCS7_set_content(PKCS7 *p7, PKCS7 *p7_data);
int PKCS7_SIGNER_INFO_set(PKCS7_SIGNER_INFO *p7i, X509 *x509, EVP_PKEY *pkey,
                          const EVP_MD *dgst);
int PKCS7_SIGNER_INFO_sign(PKCS7_SIGNER_INFO *si);
int PKCS7_add_signer(PKCS7 *p7, PKCS7_SIGNER_INFO *p7i);
int PKCS7_add_certificate(PKCS7 *p7, X509 *x509);
int PKCS7_add_crl(PKCS7 *p7, X509_CRL *x509);
int PKCS7_content_new(PKCS7 *p7, int nid);
int PKCS7_dataVerify(X509_STORE *cert_store, X509_STORE_CTX *ctx,
                     BIO *bio, PKCS7 *p7, PKCS7_SIGNER_INFO *si);
int PKCS7_signatureVerify(BIO *bio, PKCS7 *p7, PKCS7_SIGNER_INFO *si,
                          X509 *x509);

BIO *PKCS7_dataInit(PKCS7 *p7, BIO *bio);
int PKCS7_dataFinal(PKCS7 *p7, BIO *bio);
BIO *PKCS7_dataDecode(PKCS7 *p7, EVP_PKEY *pkey, BIO *in_bio, X509 *pcert);

PKCS7_SIGNER_INFO *PKCS7_add_signature(PKCS7 *p7, X509 *x509,
                                       EVP_PKEY *pkey, const EVP_MD *dgst);
X509 *PKCS7_cert_from_signer_info(PKCS7 *p7, PKCS7_SIGNER_INFO *si);
int PKCS7_set_digest(PKCS7 *p7, const EVP_MD *md);
STACK_OF(PKCS7_SIGNER_INFO) *PKCS7_get_signer_info(PKCS7 *p7);

PKCS7_RECIP_INFO *PKCS7_add_recipient(PKCS7 *p7, X509 *x509);
void PKCS7_SIGNER_INFO_get0_algs(PKCS7_SIGNER_INFO *si, EVP_PKEY **pk,
                                 X509_ALGOR **pdig, X509_ALGOR **psig);
void PKCS7_RECIP_INFO_get0_alg(PKCS7_RECIP_INFO *ri, X509_ALGOR **penc);
int PKCS7_add_recipient_info(PKCS7 *p7, PKCS7_RECIP_INFO *ri);
int PKCS7_RECIP_INFO_set(PKCS7_RECIP_INFO *p7i, X509 *x509);
int PKCS7_set_cipher(PKCS7 *p7, const EVP_CIPHER *cipher);
int PKCS7_stream(unsigned char ***boundary, PKCS7 *p7);

PKCS7_ISSUER_AND_SERIAL *PKCS7_get_issuer_and_serial(PKCS7 *p7, int idx);
ASN1_OCTET_STRING *PKCS7_digest_from_attributes(STACK_OF(X509_ATTRIBUTE) *sk);
int PKCS7_add_signed_attribute(PKCS7_SIGNER_INFO *p7si, int nid, int type,
                               void *data);
int PKCS7_add_attribute(PKCS7_SIGNER_INFO *p7si, int nid, int atrtype,
                        void *value);
ASN1_TYPE *PKCS7_get_attribute(PKCS7_SIGNER_INFO *si, int nid);
ASN1_TYPE *PKCS7_get_signed_attribute(PKCS7_SIGNER_INFO *si, int nid);
int PKCS7_set_signed_attributes(PKCS7_SIGNER_INFO *p7si,
                                STACK_OF(X509_ATTRIBUTE) *sk);
int PKCS7_set_attributes(PKCS7_SIGNER_INFO *p7si,
                         STACK_OF(X509_ATTRIBUTE) *sk);

PKCS7 *PKCS7_sign(X509 *signcert, EVP_PKEY *pkey, STACK_OF(X509) *certs,
                  BIO *data, int flags);

PKCS7_SIGNER_INFO *PKCS7_sign_add_signer(PKCS7 *p7,
                                         X509 *signcert, EVP_PKEY *pkey,
                                         const EVP_MD *md, int flags);

int PKCS7_final(PKCS7 *p7, BIO *data, int flags);
int PKCS7_verify(PKCS7 *p7, STACK_OF(X509) *certs, X509_STORE *store,
                 BIO *indata, BIO *out, int flags);
STACK_OF(X509) *PKCS7_get0_signers(PKCS7 *p7, STACK_OF(X509) *certs,
                                   int flags);
PKCS7 *PKCS7_encrypt(STACK_OF(X509) *certs, BIO *in, const EVP_CIPHER *cipher,
                     int flags);
int PKCS7_decrypt(PKCS7 *p7, EVP_PKEY *pkey, X509 *cert, BIO *data,
                  int flags);

int PKCS7_add_attrib_smimecap(PKCS7_SIGNER_INFO *si,
                              STACK_OF(X509_ALGOR) *cap);
STACK_OF(X509_ALGOR) *PKCS7_get_smimecap(PKCS7_SIGNER_INFO *si);
int PKCS7_simple_smimecap(STACK_OF(X509_ALGOR) *sk, int nid, int arg);

int PKCS7_add_attrib_content_type(PKCS7_SIGNER_INFO *si, ASN1_OBJECT *coid);
int PKCS7_add0_attrib_signing_time(PKCS7_SIGNER_INFO *si, ASN1_TIME *t);
int PKCS7_add1_attrib_digest(PKCS7_SIGNER_INFO *si,
                             const unsigned char *md, int mdlen);

int SMIME_write_PKCS7(BIO *bio, PKCS7 *p7, BIO *data, int flags);
PKCS7 *SMIME_read_PKCS7(BIO *bio, BIO **bcont);

BIO *BIO_new_PKCS7(BIO *out, PKCS7 *p7);

# ifdef  __cplusplus
}
# endif
#endif
