#############################################################################
# Generated by PAGE version 7.6
#  in conjunction with Tcl version 8.6
#  Nov 02, 2023 02:55:43 PM -03  platform: Windows NT
set vTcl(timestamp) ""
if {![info exists vTcl(borrow)]} {
    ::vTcl::MessageBox -title Error -message  "You must open project files from within PAGE."
    exit}


set image_list { 
    tanque_png "./tanque.png" 
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
        -background #a3a3a3 -highlightbackground $vTcl(actual_gui_bg) \
        -highlightcolor black 
    wm focusmodel $top passive
    wm geometry $top 1109x703+2352+164
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
    set toptitle "Tela"
    wm title $top $toptitle
    namespace eval ::widgets::${top}::ClassOption {}
    set ::widgets::${top}::ClassOption(-toptitle) $toptitle
    vTcl:DefineAlias "$top" "Tela" vTcl:Toplevel:WidgetProc "" 1
    set vTcl(real_top) {}
    canvas "$top.can50" \
        -background #868686 -closeenough 1.0 -height 633 \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -highlightthickness 0 -insertbackground black -relief ridge \
        -selectbackground #c4c4c4 -selectforeground black -width 535 
    vTcl:DefineAlias "$top.can50" "cvsTanque" vTcl:WidgetProc "Tela" 1
### SPOT dump_widget_opt A
    set site_3_0 $top.can50
    label "$site_3_0.lab51" \
        -activebackground #f9f9f9 -activeforeground SystemButtonText \
        -anchor w -background #868686 -compound left \
        -disabledforeground #868686 -font "TkDefaultFont" -foreground #ffffff \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -image tanque_png 
    vTcl:DefineAlias "$site_3_0.lab51" "imgTanque" vTcl:WidgetProc "Tela" 1
### SPOT dump_widget_opt A
    label "$site_3_0.lab52" \
        -activebackground #f9f9f9 -activeforeground SystemButtonText \
        -anchor w -background #868686 -borderwidth 0 -compound right \
        -disabledforeground #a3a3a3 \
        -font "-family Arial -size 24 -weight bold -slant roman -underline 0 -overstrike 0" \
        -foreground #0000a0 -highlightbackground $vTcl(actual_gui_bg) \
        -highlightcolor black -justify right -text "0,00" 
    vTcl:DefineAlias "$site_3_0.lab52" "lblValor" vTcl:WidgetProc "Tela" 1
### SPOT dump_widget_opt A
    label "$site_3_0.lab47" \
        -activebackground #f9f9f9 -activeforeground SystemButtonText \
        -anchor w -background #868686 -borderwidth 0 -compound left \
        -disabledforeground #a3a3a3 \
        -font "-family Arial -size 24 -weight bold -slant roman -underline 0 -overstrike 0" \
        -foreground #0000a0 -highlightbackground $vTcl(actual_gui_bg) \
        -highlightcolor black -text "m" 
    vTcl:DefineAlias "$site_3_0.lab47" "lblUnidade" vTcl:WidgetProc "Tela" 1
### SPOT dump_widget_opt A
    label "$site_3_0.lab48" \
        -activebackground #f9f9f9 -activeforeground SystemButtonText \
        -anchor w -background #868686 -borderwidth 0 -compound left \
        -disabledforeground #a3a3a3 \
        -font "-family Arial -size 24 -weight bold -slant roman -underline 0 -overstrike 0" \
        -foreground #0000a0 -highlightbackground $vTcl(actual_gui_bg) \
        -highlightcolor black -text "3" 
    vTcl:DefineAlias "$site_3_0.lab48" "lblCubo" vTcl:WidgetProc "Tela" 1
### SPOT dump_widget_opt A
    label "$site_3_0.lab50" \
        -activebackground #f9f9f9 -activeforeground SystemButtonText \
        -anchor w -background #868686 -borderwidth 0 -compound left \
        -disabledforeground #a3a3a3 \
        -font "-family Arial -size 24 -weight bold -slant roman -underline 0 -overstrike 0" \
        -foreground #0000a0 -highlightbackground $vTcl(actual_gui_bg) \
        -highlightcolor black -text "Volume:" 
    vTcl:DefineAlias "$site_3_0.lab50" "lblVolume" vTcl:WidgetProc "Tela" 1
### SPOT dump_widget_opt A
    place $site_3_0.lab51 \
        -in $site_3_0 -x 0 -relx 0.037 -y 0 -rely 0.118 -width 0 \
        -relwidth 0.927 -height 0 -relheight 0.86 -anchor nw \
        -bordermode ignore 
    place $site_3_0.lab52 \
        -in $site_3_0 -x 0 -relx 0.43 -y 0 -rely 0.034 -width 0 \
        -relwidth 0.133 -height 0 -relheight 0.054 -anchor nw \
        -bordermode ignore 
    place $site_3_0.lab47 \
        -in $site_3_0 -x 0 -relx 0.561 -y 0 -rely 0.034 -width 0 \
        -relwidth 0.065 -height 0 -relheight 0.052 -anchor nw \
        -bordermode ignore 
    place $site_3_0.lab48 \
        -in $site_3_0 -x 0 -relx 0.617 -y 0 -width 0 -relwidth 0.047 \
        -height 0 -relheight 0.069 -anchor nw -bordermode ignore 
    place $site_3_0.lab50 \
        -in $site_3_0 -x 0 -relx 0.168 -y 0 -rely 0.034 -width 0 \
        -relwidth 0.245 -height 0 -relheight 0.054 -anchor nw \
        -bordermode ignore 
    canvas "$top.can54" \
        -background #868686 -closeenough 0.0 -height 284 \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -highlightthickness 0 -insertbackground black -relief ridge \
        -selectbackground #c4c4c4 -selectforeground black -width 503 
    vTcl:DefineAlias "$top.can54" "cvsEntradas" vTcl:WidgetProc "Tela" 1
### SPOT dump_widget_opt A
    set site_3_0 $top.can54
    label "$site_3_0.lab55" \
        -activebackground #f9f9f9 -activeforeground SystemButtonText \
        -anchor w -background #868686 -compound left \
        -disabledforeground #a3a3a3 \
        -font "-family Arial -size 24 -weight normal -slant roman -underline 0 -overstrike 0" \
        -foreground #0000a0 -highlightbackground $vTcl(actual_gui_bg) \
        -highlightcolor black -text "Altura (m):" 
    vTcl:DefineAlias "$site_3_0.lab55" "lblAltura" vTcl:WidgetProc "Tela" 1
### SPOT dump_widget_opt A
    entry "$site_3_0.ent56" \
        -background white -disabledforeground #a3a3a3 \
        -font "-family Arial -size 24 -weight normal -slant roman -underline 0 -overstrike 0" \
        -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -insertbackground black -selectbackground #c4c4c4 \
        -selectforeground black -width 164 
    vTcl:DefineAlias "$site_3_0.ent56" "txtAltura" vTcl:WidgetProc "Tela" 1
### SPOT dump_widget_opt A
    label "$site_3_0.lab57" \
        -activebackground #f9f9f9 -activeforeground SystemButtonText \
        -anchor w -background #868686 -compound left \
        -disabledforeground #a3a3a3 \
        -font "-family Arial -size 24 -weight normal -slant roman -underline 0 -overstrike 0" \
        -foreground #0000a0 -highlightbackground $vTcl(actual_gui_bg) \
        -highlightcolor black -text "Diâmetro (m):" 
    vTcl:DefineAlias "$site_3_0.lab57" "lblDiametro" vTcl:WidgetProc "Tela" 1
### SPOT dump_widget_opt A
    entry "$site_3_0.ent58" \
        -background white -disabledforeground #a3a3a3 \
        -font "-family Arial -size 24 -weight normal -slant roman -underline 0 -overstrike 0" \
        -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -insertbackground black -selectbackground #c4c4c4 \
        -selectforeground black -width 164 
    vTcl:DefineAlias "$site_3_0.ent58" "txtDiametro" vTcl:WidgetProc "Tela" 1
### SPOT dump_widget_opt A
    button "$site_3_0.but59" \
        -activebackground $vTcl(analog_color_m) -activeforeground black \
        -background #b0b0b0 -command "enviar" -compound center \
        -disabledforeground #a3a3a3 \
        -font "-family Arial -size 24 -weight normal -slant roman -underline 0 -overstrike 0" \
        -foreground #0000a0 -highlightbackground $vTcl(actual_gui_bg) \
        -highlightcolor black -pady 0 -text "Enviar" 
    vTcl:DefineAlias "$site_3_0.but59" "btnEnviar" vTcl:WidgetProc "Tela" 1
### SPOT dump_widget_opt A
    place $site_3_0.lab55 \
        -in $site_3_0 -x 0 -relx 0.099 -y 0 -rely 0.166 -width 0 \
        -relwidth 0.326 -height 0 -relheight 0.106 -anchor nw \
        -bordermode ignore 
    place $site_3_0.ent56 \
        -in $site_3_0 -x 0 -relx 0.537 -y 0 -rely 0.141 -width 164 \
        -relwidth 0 -height 40 -relheight 0 -anchor nw -bordermode ignore 
    place $site_3_0.lab57 \
        -in $site_3_0 -x 0 -relx 0.099 -y 0 -rely 0.389 -width 0 \
        -relwidth 0.406 -height 0 -relheight 0.106 -anchor nw \
        -bordermode ignore 
    place $site_3_0.ent58 \
        -in $site_3_0 -x 0 -relx 0.537 -y 0 -rely 0.389 -width 164 \
        -relwidth 0 -height 40 -relheight 0 -anchor nw -bordermode ignore 
    place $site_3_0.but59 \
        -in $site_3_0 -x 0 -relx 0.358 -y 0 -rely 0.707 -width 137 \
        -relwidth 0 -height 44 -relheight 0 -anchor nw -bordermode ignore 
    canvas "$top.can60" \
        -background #868686 -closeenough 1.0 -height 70 \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -highlightthickness 0 -insertbackground black -relief ridge \
        -selectbackground #c4c4c4 -selectforeground black -width 503 
    vTcl:DefineAlias "$top.can60" "cvsTitulo" vTcl:WidgetProc "Tela" 1
### SPOT dump_widget_opt A
    set site_3_0 $top.can60
    label "$site_3_0.lab61" \
        -activebackground #f9f9f9 -activeforeground SystemButtonText \
        -anchor w -background #868686 -borderwidth 0 -compound center \
        -disabledforeground #a3a3a3 \
        -font "-family Arial -size 24 -weight bold -slant roman -underline 0 -overstrike 0" \
        -foreground #0000a0 -highlightbackground $vTcl(actual_gui_bg) \
        -highlightcolor black -text "Cálculo de Volume do Tanque" 
    vTcl:DefineAlias "$site_3_0.lab61" "lblTitulo" vTcl:WidgetProc "Tela" 1
### SPOT dump_widget_opt A
    place $site_3_0.lab61 \
        -in $site_3_0 -x 0 -relx 0.02 -y 0 -rely 0.294 -width 0 \
        -relwidth 0.922 -height 0 -relheight 0.544 -anchor nw \
        -bordermode ignore 
    ###################
    # SETTING GEOMETRY
    ###################
    place $top.can50 \
        -in $top -x 0 -relx 0.505 -y 0 -rely 0.128 -width 0 -relwidth 0.482 \
        -height 0 -relheight 0.841 -anchor nw -bordermode ignore 
    place $top.can54 \
        -in $top -x 0 -relx 0.027 -y 0 -rely 0.354 -width 0 -relwidth 0.454 \
        -height 0 -relheight 0.392 -anchor nw -bordermode ignore 
    place $top.can60 \
        -in $top -x 0 -relx 0.027 -y 0 -rely 0.142 -width 0 -relwidth 0.454 \
        -height 0 -relheight 0.096 -anchor nw -bordermode ignore 

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

