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
  int port_id;
  char buf[SOCKET_BUF_MAXLINE+2];
  

} svfr_sock_server;

static svfr_sock_server * create_sock_server() {
  svfr_sock_server * sh =   (svfr_sock_server *) malloc( sizeof(svfr_sock_server));
  
  //creation of the socket
  sh->listenfd = socket (AF_INET, SOCK_STREAM, 0);
  sh->connfd = 0;

  return sh;
}

static int get_port_id(svfr_sock_server * sh) {
   return sh->port_id;
}

static int bind_sock_server(svfr_sock_server *sh, int port_id) {

  //preparation of the socket address
  sh->servaddr.sin_family = AF_INET;
  sh->servaddr.sin_addr.s_addr = htonl(INADDR_ANY);
  sh->servaddr.sin_port = htons(port_id);
  sh->port_id = port_id;
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

static int accept_sock_server(svfr_sock_server *sh) {
  struct sockaddr_in cliaddr;
  int clilen = sizeof(cliaddr);
  sh->connfd = accept (sh->listenfd, (struct sockaddr *) &cliaddr, &clilen);
  if (sh->connfd < 0){
    /** perror("accept error"); **/
    return sh->connfd;
  }
  return 0;
}

static char * recv_sock_server(svfr_sock_server *sh) {
  int n = recv(sh->connfd, sh->buf, SOCKET_BUF_MAXLINE, 0);
  if (n <= 0) {
     //  printf("recv error\n");
     sh->buf[0] = 0;
  }    
     
  sh->buf[n-1] = 0;
  return sh->buf;
}

static int send_sock_server(svfr_sock_server * sh, char * buf) {
  return send(sh->connfd, buf, strlen(buf), 0);
}

static void close_sock_server(svfr_sock_server * sh) {
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

#define SVFR_OPEN_TRY_CNT 100

end #;

// type sock_error: [ OPEN_ALREADY_IN_USE ];

// define svfr__first_port_id 4321;

struct svfr_sock_server {
    socket_h: external_pointer;

    open(port_id: int): int is  C code #:
        me->socket_h = create_sock_server();
	result = bind_sock_server(me->socket_h, port_id);	
    end #;

    open_any_port(start_from: int = 4321 ): int is C code #:
        int i;
        svfr_sock_server * sh = create_sock_server();
        sh->port_id = 0;
        me->socket_h = sh;
        for (i= start_from; i < (start_from + SVFR_OPEN_TRY_CNT); i++) {
            result = bind_sock_server(sh, i);
            if (result == 0) {
               break;
            }
        }
        if (result == 0) {
             sh->port_id = i;
        }

    end #;


    get_port_id(): int is C code #:
         result =  get_port_id(me->socket_h);
    end #;

    bind(port_id: int): int is C code #:
        result = bind_sock_server(me->socket_h, port_id);
    end #;

    accept(): int is C code #:
        result = accept_sock_server(me->socket_h);
    end #;

    read(): string is C code #:
        result = ts1(recv_sock_server(me->socket_h));
    end #;

    write(buf: string): int is C code #:
        result = send_sock_server(me->socket_h, buf);
    end #;
    
    close() is C code #:
        close_sock_server(me->socket_h);
	me->socket_h = NULL;
    end #;

    lines: list of string;
    ind: int;
    read_line(): string is {
         
        var buf: string;
        if lines.size() == 0 {
	    buf = read();
            print buf;
	    if str_len(buf) == 0 {
	         // error
		 return "ERROR";  // TODO ????? 
            };
	    lines = str_split(buf, "\n");
	    print lines;
// TODO check that the last string is full or nee to keep it to next read
	    ind = 0;
	 };
	 result = lines[ind];
	 if ind == lines.size() -1 {
	     lines.clear();
	     ind = 0;
	 } else {
	   ind +=1;
	 };
    };
   
    write_line(line: string): int is {
        // return write(line);
	var tmp: string =appendf("%s\n",line);
	outf("Write line: %d\n", str_len(tmp));
	return write(tmp)
    };
};

extend global {

    // server echo example
    sock_server(port_id: int) is {
        var status : int;
        var buf : string;

	var sh := new svfr_sock_server;
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
