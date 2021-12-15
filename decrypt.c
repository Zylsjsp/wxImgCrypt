#include <stdio.h>
#include <string.h>

#define BYTE unsigned char

int main(int argc, char **argv)
{
    char *f1=argv[1], *f2=argv[2];
    // strncmp(f1, argv[0], strchr(argv[0], '.')-argv[0]);
    // strncmp(f2, argv[1], strchr(argv[1], '.')-argv[1]);

    FILE *fp1=fopen(f1,"rb");
    FILE *fp2=fopen(f2,"wb");
    BYTE buffer[16]={};
    BYTE hByte[2]={};
    fread(hByte, sizeof(BYTE), 2, fp1);
    fseek(fp1, 0, SEEK_SET);
    BYTE header[2]={0xff, 0xd8};
    for (int i=0; i < 2; i++)
    {
        hByte[i]=hByte[i] ^ header[i];
    }
    if (hByte[0] != hByte[1])
    {
        printf("Not valid WeChat data!\nExiting...\n");
        fclose(fp1);
        fclose(fp2);
        return -1;
    }
    BYTE wd=hByte[0];
    int i=0;
    while (16==(i=fread(buffer, sizeof(BYTE), 16, fp1)))
    {
        for (int i=0; i < 16; i++)
        {
            buffer[i]=buffer[i] ^ wd;
        }
        fwrite(buffer, sizeof(BYTE), 16, fp2);

    }
    fwrite(buffer, sizeof(BYTE), i, fp2);
    printf("Successfully decrypted!\n");
    fclose(fp1);
    fclose(fp2);
    return 0;
}
