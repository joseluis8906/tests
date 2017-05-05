#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <openssl/sha.h>
#include <openssl/hmac.h>
#include <openssl/evp.h>
#include <openssl/bio.h>
#include <openssl/buffer.h>
#include <time.h>
#include <math.h>


int PasswordEncrypt (const char *Src, char *Dest)
{
    time_t Seconds;
    time (&Seconds);	
    srand ((unsigned int) Seconds);
	
    char Alpha[] = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ";
    int Index = rand () % 62;
	
    char Character[]="abcdefgh";
    Character[0] = Alpha[Index];
    printf ("%s\n", Character);
    unsigned char Hash[SHA256_DIGEST_LENGTH];

    SHA256 ((unsigned char*)Character, strlen (Character), Hash);
	
    char RandomDigest[(SHA256_DIGEST_LENGTH * 2) + 1];
    int i = 0;
    for (i = 0; i < SHA256_DIGEST_LENGTH; i++)
    {
        sprintf (RandomDigest + (i * 2), "%02x", (int)Hash[i]);
    }
    
    char Salt[17];
    snprintf (Salt, 17, RandomDigest);
    
    Salt[6] = Character[0];
    
    char SrcModified[64];
    strncpy (SrcModified, Src, 64);
    SrcModified[4] = Character[0];
    
    SHA256 ((unsigned char*)SrcModified, strlen (SrcModified), Hash);

    char DigestSrcModified[(SHA256_DIGEST_LENGTH * 2) + 1];
    
    for (i = 0; i < SHA256_DIGEST_LENGTH; i++)
    {
        sprintf (DigestSrcModified + (i * 2), "%02x", (int)Hash[i]);
    }

    strcpy (Dest, "sha256$");
    strcat (Dest, Salt);
    strcat (Dest, "$");
    strcat (Dest, DigestSrcModified);
    
    return 0;
}

int CheckPassword (const char *Original, const char *Crypted)
{
    char Character[]="abcdefgh";
    Character[0] = *(Crypted+13);
    printf ("%s\n", Character);
    unsigned char Hash[SHA256_DIGEST_LENGTH];

    SHA256 ((unsigned char*)Character, strlen (Character), Hash);
	
    char RandomDigest[(SHA256_DIGEST_LENGTH * 2) + 1];
    int i = 0;
    for (i = 0; i < SHA256_DIGEST_LENGTH; i++)
    {
        sprintf (RandomDigest + (i * 2), "%02x", (int)Hash[i]);
    }
    
    char Salt[17];
    snprintf (Salt, 17, RandomDigest);
    
    Salt[6] = Character[0];
    
    char SrcModified[64];
    strncpy (SrcModified, Original, 64);
    SrcModified[4] = Character[0];
     
    SHA256 ((unsigned char*)SrcModified, strlen (SrcModified), Hash);

    char DigestSrcModified[(SHA256_DIGEST_LENGTH * 2) + 1];
    
    for (i = 0; i < SHA256_DIGEST_LENGTH; i++)
    {
        sprintf (DigestSrcModified + (i * 2), "%02x", (int)Hash[i]);
    }
    
    char Result[88];
    
    strcpy (Result, "sha256$");
    strcat (Result, Salt);
    strcat (Result, "$");
    strcat (Result, DigestSrcModified);

    int Ret;
    printf ("%s\n", Result);
    if (strcmp (Result, Crypted) == 0)
    {
        Ret = 1;
    }
    else
    {
        Ret = 0;
    }
    
    return Ret;
}

int main ()
{
    char Original[128];
    char Crypted[128];
    
    strcpy (Original, "7295");
    //strcpy (Crypted, "sha256$72dfcfL0c470ac25$b0ac6336ed6d81567abb146ffeb69b834c2552cab77043398cab9bced376337d");
    PasswordEncrypt(Original, Crypted);
    printf ("%s\n", Crypted);
    /*
    if (CheckPassword("7295", Crypted))
    {
        printf ("funciona");
    }
    else 
    {
        printf ("no funciona");
    }*/
    return 0;
}
