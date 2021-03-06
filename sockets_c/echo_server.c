#include <stdlib.h>
#include <stdio.h>
#include <sys/types.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <string.h>
#include <unistd.h>

#define MAXLINE 4096+2/*max text line length*/

/** #define SERV_PORT 3000 port **/
#define LISTENQ 5 /*maximum number of client connections */

int main (int argc, char **argv)
{
  int listenfd, connfd, n;
  socklen_t clilen;
  char buf[MAXLINE+2];
  
  struct sockaddr_in cliaddr, servaddr;
  
  //creation of the socket
  listenfd = socket (AF_INET, SOCK_STREAM, 0);
  
  //preparation of the socket address
  servaddr.sin_family = AF_INET;
  servaddr.sin_addr.s_addr = htonl(INADDR_ANY);
  servaddr.sin_port = htons(atoi(argv[1]));
  
  if (bind (listenfd, (struct sockaddr *) &servaddr, sizeof(servaddr)) != 0) {
    perror("Bind error");
    exit(123);
  }
  
  if (listen (listenfd, LISTENQ) != 0) {
    perror("Listen error");
    exit(124);
  }
  
  printf("%s\n","Server running...waiting for connections.");
  
  for ( ; ; ) {
    
    clilen = sizeof(cliaddr);
    connfd = accept (listenfd, (struct sockaddr *) &cliaddr, &clilen);
    if (connfd < 0){
      perror("accept error");
      continue;
    }
      
    printf("%s\n","Received request...");
    
    while ( (n = recv(connfd, buf, MAXLINE,0)) > 0)  {
      printf("%s(%d)","String received from and resent to the client:",n);
      puts(buf);
      send(connfd, buf, n, 0);
    }
    
    if (n < 0) {
      perror("Read error");
      exit(1);
    }
    close(connfd);
    
  }
  
  //close listening socket
  close (listenfd);
}

