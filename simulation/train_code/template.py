def set_template(args):
    # Set the template
    if args.template.find('hfwg_mdsgnet') >= 0:
        args.input_setting = 'H'
        args.input_mask = 'Phi'