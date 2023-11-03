#############################################################################
# Generated by PAGE version 7.6
#  in conjunction with Tcl version 8.6
#  Nov 02, 2023 12:24:11 AM -03  platform: Windows NT
set vTcl(timestamp) ""
if {![info exists vTcl(borrow)]} {
    ::vTcl::MessageBox -title Error -message  "You must open project files from within PAGE."
    exit}


set image_list { 
}
vTcl:create_project_images $image_list   ;# In image.tcl

if {!$vTcl(borrow) && !$vTcl(template)} {

set vTcl(actual_gui_font_dft_desc)  TkDefaultFont
set vTcl(actual_gui_font_dft_name)  TkDefaultFont
set vTcl(actual_gui_font_text_desc)  TkTextFont
set vTcl(actual_gui_font_text_name)  TkTextFont
set vTcl(actual_gui_font_fixed_desc)  TkFixedFont
set vTcl(actual_gui_font_fixed_name)  TkFixedFont
set vTcl(actual_gui_font_menu_desc)  TkMenuFont
set vTcl(actual_gui_font_menu_name)  TkMenuFont
set vTcl(actual_gui_font_tooltip_desc)  TkDefaultFont
set vTcl(actual_gui_font_tooltip_name)  TkDefaultFont
set vTcl(actual_gui_font_treeview_desc)  TkDefaultFont
set vTcl(actual_gui_font_treeview_name)  TkDefaultFont
########################################### 
set vTcl(actual_gui_bg) #d9d9d9
set vTcl(actual_gui_fg) #000000
set vTcl(actual_gui_analog) #ececec
set vTcl(actual_gui_menu_analog) #ececec
set vTcl(actual_gui_menu_bg) #d9d9d9
set vTcl(actual_gui_menu_fg) #000000
set vTcl(complement_color) gray40
set vTcl(analog_color_p) #c3c3c3
set vTcl(analog_color_m) beige
set vTcl(tabfg1) black
set vTcl(tabfg2) black
set vTcl(actual_gui_menu_active_bg)  #ececec
set vTcl(actual_gui_menu_active_fg)  #000000
########################################### 
set vTcl(pr,autoalias) 1
set vTcl(pr,relative_placement) 1
set vTcl(mode) Relative
}




proc vTclWindow.top1 {base} {
    global vTcl
    if {$base == ""} {
        set base .top1
    }
    if {[winfo exists $base]} {
        wm deiconify $base; return
    }
    set top $base
    set target $base
    ###################
    # CREATING WIDGETS
    ###################
    vTcl::widgets::core::toplevel::createCmd $top -class Toplevel \
        -background #ffffff -highlightbackground $vTcl(actual_gui_bg) \
        -highlightcolor black 
    wm focusmodel $top passive
    wm geometry $top 600x450+2183+519
    update
    # set in toplevel.wgt.
    global vTcl
    global img_list
    set vTcl(save,dflt,origin) 0
    wm maxsize $top 3844 1061
    wm minsize $top 120 1
    wm overrideredirect $top 0
    wm resizable $top 1 1
    wm deiconify $top
    set toptitle "Principal"
    wm title $top $toptitle
    namespace eval ::widgets::${top}::ClassOption {}
    set ::widgets::${top}::ClassOption(-toptitle) $toptitle
    vTcl:DefineAlias "$top" "Principal" vTcl:Toplevel:WidgetProc "" 1
    set vTcl(real_top) {}
    button "$top.but48" \
        -activebackground $vTcl(analog_color_m) -activeforeground #ffffff \
        -background #0080ff -command "cliquebtnEnviar" -compound center \
        -disabledforeground #a3a3a3 \
        -font "-family {Segoe UI} -size 16 -weight normal -slant roman -underline 0 -overstrike 0" \
        -foreground #ffffff -highlightbackground $vTcl(actual_gui_bg) \
        -highlightcolor #ffffff -pady 0 -text "Enviar" 
    vTcl:DefineAlias "$top.but48" "btnEnviar" vTcl:WidgetProc "Principal" 1
### SPOT dump_widget_opt A
    bind $top.but48 <Button-1> {
        lambda e: clique_btnEnviar(e)
    }
    label "$top.lab49" \
        -activebackground #f9f9f9 -activeforeground SystemButtonText \
        -anchor w -background #ffffff -compound center \
        -disabledforeground #a3a3a3 \
        -font "-family {Segoe UI} -size 18 -weight bold -slant roman -underline 0 -overstrike 0" \
        -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -text "Login" 
    vTcl:DefineAlias "$top.lab49" "lblLogin" vTcl:WidgetProc "Principal" 1
### SPOT dump_widget_opt A
    entry "$top.ent50" \
        -background white -disabledforeground #a3a3a3 \
        -font "-family {Courier New} -size 16 -weight normal -slant roman -underline 0 -overstrike 0" \
        -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -insertbackground black -selectbackground #c4c4c4 \
        -selectforeground black -textvariable "txtLogin" -width 254 
    vTcl:DefineAlias "$top.ent50" "txtLogin" vTcl:WidgetProc "Principal" 1
### SPOT dump_widget_opt A
    label "$top.lab51" \
        -activebackground #f9f9f9 -activeforeground SystemButtonText \
        -anchor w -background #ffffff -compound center \
        -disabledforeground #a3a3a3 \
        -font "-family {Segoe UI} -size 18 -weight bold -slant roman -underline 0 -overstrike 0" \
        -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -text "Senha" 
    vTcl:DefineAlias "$top.lab51" "lblSenha" vTcl:WidgetProc "Principal" 1
### SPOT dump_widget_opt A
    entry "$top.ent52" \
        -background white -disabledforeground #a3a3a3 \
        -font "-family {Courier New} -size 16 -weight normal -slant roman -underline 0 -overstrike 0" \
        -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -insertbackground black -selectbackground #c4c4c4 \
        -selectforeground black -textvariable "txtSenha" -width 254 
    vTcl:DefineAlias "$top.ent52" "txtSenha" vTcl:WidgetProc "Principal" 1
### SPOT dump_widget_opt A
    ###################
    # SETTING GEOMETRY
    ###################
    place $top.but48 \
        -in $top -x 0 -relx 0.367 -y 0 -rely 0.422 -width 147 -relwidth 0 \
        -height 34 -relheight 0 -anchor nw -bordermode ignore 
    place $top.lab49 \
        -in $top -x 0 -relx 0.433 -y 0 -rely 0.067 -width 0 -relwidth 0.123 \
        -height 0 -relheight 0.091 -anchor nw -bordermode ignore 
    place $top.ent50 \
        -in $top -x 0 -relx 0.3 -y 0 -rely 0.156 -width 254 -relwidth 0 \
        -height 20 -relheight 0 -anchor nw -bordermode ignore 
    place $top.lab51 \
        -in $top -x 0 -relx 0.433 -y 0 -rely 0.244 -width 0 -relwidth 0.123 \
        -height 0 -relheight 0.091 -anchor nw -bordermode ignore 
    place $top.ent52 \
        -in $top -x 0 -relx 0.3 -y 0 -rely 0.333 -width 254 -relwidth 0 \
        -height 20 -relheight 0 -anchor nw -bordermode ignore 

    vTcl:FireEvent $base <<Ready>>
}

proc 36 {args} {return 1}


Window show .
set btop1 ""
if {$vTcl(borrow)} {
    set btop1 .bor[expr int([expr rand() * 100])]
    while {[lsearch $btop1 $vTcl(tops)] != -1} {
        set btop1 .bor[expr int([expr rand() * 100])]
    }
}
set vTcl(btop) $btop1
Window show .top1 $btop1
if {$vTcl(borrow)} {
    $btop1 configure -background plum
}

