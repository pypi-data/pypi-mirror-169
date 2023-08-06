# UniVISA Library
This library provide universal access to devices, which can get commands from PC by VISA.
You can send your own commands to device, or create configuration file with procedures. 
##### Model-file template:
~~~
{
    "info": {
        "vendor": vendor_name,
        "model": device_model,
        "port_num": port_num
    },

    "config": {
        "address": device_address,
        "timeout": timeout,
        "termination": termination_symbol,
        "log_level": log_level
    },

    "procedure": {
        procedure_name: [
            {
                "cmd": cmd_1,
                "args": arg_names_list
            },
            {
                "cmd": cmd_2,
                "args": arg_names_list
            },
            ...,
            {
                "cmd": cmd_n,
                "args": arg_names_list
            }
        ]
    }
}

log_level should be:
1) none
2) err
3) opc
4) opc_and_err

~~~