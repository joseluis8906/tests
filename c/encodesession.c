#include <stdio.h>
#include <string.h>

int func (const char *PseudoId, char *SessionId)
{
    char Dict[] = "0X1P2QV4cCUdeAfgMhijEklmnS5OpZqrKsWt9vIw7by6zBu-DF3Hx8JaL_@NRo.TYG";
    int DictLen = strlen (Dict);
    int i = 0;
    int Len = strlen (PseudoId);
    char *Pch;
    int Index;
    
    for (i = 0; i < Len; i++)
    {
        Pch = strrchr(Dict, PseudoId[i]);
        Index = Pch-Dict;
        Index += 13;
        
        if (Index > (DictLen - 1))
        {
            Index -= DictLen;
        }
        
        SessionId[i] = Dict[Index];
    }
    SessionId[Len] = '\0';

    return 0;
}

int main (void)
{
    char SessionId[64];
    func ("joseluis8906@opmbx.org", SessionId);
    printf ("%s\n", SessionId);

    return 0;
}
