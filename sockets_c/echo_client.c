

#include <stdlib.h>
#include <stdio.h>
#include <sys/types.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <string.h>
#include <arpa/inet.h>


#define MAXLINE 4096 /*max text line length*/
#define SERV_PORT 3000 /*port*/


int
main(int argc, char **argv)
{
  int sockfd;
  int n;
  struct sockaddr_in servaddr;
  char sendline[MAXLINE+2], recvline[MAXLINE+2];
  //basic check of the arguments
  //additional checks can be inserted
  if (argc !=2) {
    perror("Usage: TCPClient <IP address of the server");
    exit(1);
  }
  
  //Create a socket for the client
  //If sockfd<0 there was an error in the creation of the socket
  if ((sockfd = socket (AF_INET, SOCK_STREAM, 0)) <0) {
    perror("Problem in creating the socket");
    exit(2);
  }
  
  //Creation of the socket
  memset(&servaddr, 0, sizeof(servaddr));
  servaddr.sin_family = AF_INET;
  //servaddr.sin_addr.s_addr= inet_addr(argv[1]);
  servaddr.sin_addr.s_addr= inet_addr("127.0.0.1");
  
  servaddr.sin_port =  htons(atoi(argv[1])); //convert to big-endian order
  
  //Connection of the client to the socket
  if (connect(sockfd, (struct sockaddr *) &servaddr, sizeof(servaddr))<0) {
    perror("Problem in connecting to the server");
    exit(3);
  }
  
  while (fgets(sendline, MAXLINE, stdin) != NULL) {
    
    send(sockfd, sendline, strlen(sendline)+1, 0);
    
    if ( ( n=recv(sockfd, recvline, MAXLINE,0)) == 0){
      //error: server terminated prematurely
      perror("The server terminated prematurely");
      exit(4);
    }
    int n1 = strlen(recvline);
    printf("%s(%d,%d,  %d %d)", "String received from the server: ", n, n1, (int)recvline[n-1], (int) recvline[n]);
    // recvline[n-1] =0;
    fputs(recvline, stdout);
    // fputs("\n", stdout);
  }
  
  exit(0);
}

