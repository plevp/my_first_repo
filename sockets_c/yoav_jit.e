<'
// this is copy-paste code from perspec
extend sn_C_compilation {
    compile_to_shlib(c_file: string, so_file: string): sn_library is {
        var shell_cmd : string;
        var path_so_file : string;
        var shell_result : list of string;
        var obj_file: string = get_object_filename(c_file);
        
        if (!flags_init) {
            init_flags();
        };
                
        shell_cmd = get_compile_command(c_file,obj_file,"");
	print shell_cmd;
        c_comp_debug(appendf("Compilation command: %s",shell_cmd));
        shell_result = output_from_check(shell_cmd);
        
        //shell_cmd = get_link_command(obj_file,so_file);
	shell_cmd = appendf("%s %s %s -o %s",specman_linker,specman_shlib_ldflags,obj_file,so_file);
	print shell_cmd;
        c_comp_debug(append("Linking command: ",shell_cmd));
        shell_result = output_from_check(shell_cmd);
        
        shlibs.prepend_dir_to_search_path(get_lib_path());
        result = shlibs.open(so_file,NULL,lazy,global);    
    };
};

extend JIT_comp {
    compile_file(c_file: string) is {
      //  c_compilation.set_debug_mode(TRUE);
	var file_name: = files.new_temp_file();
	print file_name;
        shared_library = c_compilation.compile_to_shlib(c_file, appendf("%sso", file_name));
    };
};




// this is user code
extend sys {
    !jit_comp: JIT_comp;
     
    foo(s: string): string is foreign dynamic C routine;
    
    write_jit() is {
        if (jit_comp == NULL) {
            // var code: list of string = {" int foo() {"; " printf(\"In foo\\n\");"; " return 5;"; "}"}; 
            var code: list of string = {" int foo(char * s) {"; " return ts1(s);"; "}"}; 
            jit_comp = new;
            var top_filename: string = "yoav_example.c";
            files.write_string_list(top_filename, code);
            jit_comp.compile_file(top_filename);
        };
    };
    
    run() is also {
        write_jit();
        print foo("");
    };
};

'>
