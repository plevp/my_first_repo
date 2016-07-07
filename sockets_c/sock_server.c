
#include <stdlib.h>
#include <stdio.h>
#include <sys/types.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <string.h>
#include <unistd.h>
#include <errno.h>

#define SOCKET_BUF_MAXLINE 4096+2/*max text line length*/

/** #define SERV_PORT 3000 port **/
#define LISTENQ 8 /*maximum number of client connections */


typedef struct {
  struct sockaddr_in servaddr;
  int listenfd;
  int connfd;
  char buf[SOCKET_BUF_MAXLINE+2];

} frtl_sock_server;

static frtl_sock_server * create_sock_server() {
  frtl_sock_server * sh =   (frtl_sock_server *) malloc( sizeof(frtl_sock_server));
  
  //creation of the socket
  sh->listenfd = socket (AF_INET, SOCK_STREAM, 0);
  sh->connfd = 0;

  return sh;
}

static int bind_sock_server(frtl_sock_server *sh, int port_id) {

  //preparation of the socket address
  sh->servaddr.sin_family = AF_INET;
  sh->servaddr.sin_addr.s_addr = htonl(INADDR_ANY);
  sh->servaddr.sin_port = htons(port_id);
  
  if (bind (sh->listenfd, (struct sockaddr *) &(sh->servaddr), sizeof(sh->servaddr)) != 0) {
    /** perror("Bind error"); **/
    return errno;
  }
  
  if (listen (sh->listenfd, LISTENQ) != 0) {
    /** perror("Listen error"); **/
    return errno;
  }
  
  return 0;
}

static int accept_sock_server(frtl_sock_server *sh) {
  struct sockaddr_in cliaddr;
  int clilen = sizeof(cliaddr);
  sh->connfd = accept (sh->listenfd, (struct sockaddr *) &cliaddr, &clilen);
  if (sh->connfd < 0){
    /** perror("accept error"); **/
    return sh->connfd;
  }
  return 0;
}

static char * recv_sock_server(frtl_sock_server *sh) {
  recv(sh->connfd, sh->buf, SOCKET_BUF_MAXLINE, 0);
  return sh->buf;
}

static void send_sock_server(frtl_sock_server * sh, char * buf) {
  send(sh->connfd, buf, strlen(buf)+1, 0);
}

static void close_sock_server(frtl_sock_server * sh) {
  if (sh == NULL)  return;

  if( sh->listenfd != 0) {
    close(sh->listenfd);
    sh->listenfd = 0;
  }
  if (sh->connfd != 0) {
    close(sh->connfd);
    sh->connfd = 0 ;
  }
  free (sh);
}

int main(int argc, char **argv) {
  frtl_sock_server * my_socket = create_sock_server();
  int status = bind_sock_server(my_socket, atoi(argv[1]));

  printf("%s\n","Server running...waiting for connections.");

  for ( ; ; ) {
    status = accept_sock_server(my_socket);
    if (status != 0 ) 
      continue;

    printf("%s\n","Received request...");
    
    char * buf;
    while (  (buf = recv_sock_server(my_socket)) != 0)  {
      // if (buf[0] == '*') break;
      printf("%s","String received from and resent to the client:");
      puts(buf);
      send_sock_server(my_socket, buf);
      
    }
    // if (buf[0] == '*') break;

  }

  close_sock_server(my_socket);
  my_socket = NULL;
  return 0;
}
