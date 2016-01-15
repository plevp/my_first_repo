<'

C code #:
#include <stdlib.h>
#include <stdio.h>
#include <sys/types.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <string.h>
#include <unistd.h>
#include <errno.h>

#define SOCKET_BUF_MAXLINE 4096+2/*max text line length*/
#define LISTENQ 8 

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
  int n = recv(sh->connfd, sh->buf, SOCKET_BUF_MAXLINE, 0);
  if (n < 0) {
     //  printf("recv error\n");
     sh->buf[0] = 0;
  }    
  
  return sh->buf;
}

static int send_sock_server(frtl_sock_server * sh, char * buf) {
  return send(sh->connfd, buf, strlen(buf)+1, 0);
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


end #;

// type sock_error: [ OPEN_ALREADY_IN_USE ];

struct frtl_sock_server {
    socket_h: external_pointer;

    open(port_id: int): int is  C code #:
        me->socket_h = create_sock_server();
	result = bind_sock_server(me->socket_h, port_id);	
    end #;

    bind(port_id: int): int is C code #:
        result = bind_sock_server(me->socket_h, port_id);
    end #;

    accept(): int is C code #:
        result = accept_sock_server(me->socket_h);
    end #;

    read(): string is C code #:
        result = sf(recv_sock_server(me->socket_h));
    end #;

    write(buf: string): int is C code #:
        result = send_sock_server(me->socket_h, buf);
    end #;
    
    close() is C code #:
        close_sock_server(me->socket_h);
	me->socket_h = NULL;
    end #;
};

extend global {

    sock_server(port_id: int) is {
        var status : int;
        var buf : string;

	var sh := new frtl_sock_server;
	status = sh.open(port_id);
	if status != 0 {
	    outf("Open socket server failed with code %d, exit....\n", status );
	    return;
	};	
	outf("%s \n","Server running...waiting for connections.");
      
	while (TRUE) {
	    status = sh.accept();
	    if (status != 0) { 
	       outf("Accept failed with code %d, exit....\n", status );
	       break;
	    };
	    outf("%s\n","Received request...");
	    
	    while (TRUE) {
	        buf = sh.read();
		if str_empty(buf) {break; };
		outf("%s(%d)","String received from and resent to the client:", str_len(buf));
                out(buf);
		if sh.write(buf) == -1 {
		   break;
		};
	    };
        };
	sh.close();
    };
};

'>
