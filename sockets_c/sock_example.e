<'

extend global {


    sock_example() is {
        var status : int;
	var line : string;

	var sock1 := new svfr_sock_server;
	status = sock1.open_any_port();
	
	if status != 0 {
	   outf("Error: cannot open socket 1\n");
	   return;
	};

	var port1: int = sock1.get_port_id();
	var sock2 := new svfr_sock_server;
	status = sock2.open_any_port(port1+1);

	if status != 0 {
	   outf("Error: cannot open socket 2\n");
	   return;
	};
	var port2: int = sock2.get_port_id();

	outf(" Input port: %d\nOutput port: %d\n", port1, port2);

	status = sock1.accept();
	if (status != 0) { 
	       outf("input: Accept failed with code %d, exit....\n", status );
	};

	status = sock2.accept();
	if (status != 0) { 
	       outf("Output: Accept failed with code %d, exit....\n", status );
	};

	outf("%s\n","Received request...");
        while TRUE {
	    line = sock1.read_line();
	    
	    outf("Line: %s\n", line);
	    if line == "ERROR" {
	        break; // error 
	    };
	    outf("String received from and resent to the client: %s (%d)\n",line, str_len(line));
	    
	    status = sock2.write_line(line);
	    if status < 0 {
	        break;  // error
            }; 
        };	
		
    };
};


'>
