#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>
#include <openssl/sha.h>
#include <openssl/hmac.h>
#include <openssl/evp.h>
#include <openssl/bio.h>
#include <openssl/buffer.h>

int Base64Encode (const char *Original, char *Encoded);

int Base64Encode(const char *Original, char *Encoded) //Encodes a string to base64
{
    BIO *bmem, *b64;
    BUF_MEM *bptr;

    b64 = BIO_new(BIO_f_base64());
    bmem = BIO_new(BIO_s_mem());
    b64 = BIO_push(b64, bmem);
    BIO_write(b64, Original, strlen(Original));
    BIO_flush(b64);
    BIO_get_mem_ptr(b64, &bptr);

    memcpy (Encoded, bptr->data, bptr->length-1);
    Encoded [bptr->length-1] = '\0';

    BIO_free_all(b64);

    return 0; //success
}

int main (void)
{
    char Encoded [256];
    char Original [128];
    char Num [64];

    strcpy (Original, "C.C_1098671330");
    sprintf (Num, "_%d", (int)time(NULL));
    strcat (Original, Num);
    
    printf ("%s\n", Original);

    Base64Encode (Original, Encoded);

    printf ("%s\n", Encoded);

    printf ("%lld\n", 9223372036854775807);
}
