#############################################################################
# Generated by PAGE version 7.6
#  in conjunction with Tcl version 8.6
#  Nov 02, 2023 11:23:38 AM -03  platform: Windows NT
set vTcl(timestamp) ""
if {![info exists vTcl(borrow)]} {
    ::vTcl::MessageBox -title Error -message  "You must open project files from within PAGE."
    exit}


set image_list { 
    motor1_png "./atividade2/images/motor1.png" 
    motor1_png "./atividade2/images/motor1.png" 
    puc2_png "./atividade2/images/PUC2.png" 
    tanques2_png "./atividade2/images/tanques2.png" 
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
        -menu "$top.m49" -relief groove -background #303030 \
        -highlightbackground #FFFFFF -highlightcolor black 
    wm focusmodel $top passive
    wm geometry $top 1022x854+2289+98
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
    set toptitle "Tela Principal"
    wm title $top $toptitle
    namespace eval ::widgets::${top}::ClassOption {}
    set ::widgets::${top}::ClassOption(-toptitle) $toptitle
    vTcl:DefineAlias "$top" "TelaPrincipal" vTcl:Toplevel:WidgetProc "" 1
    set vTcl(real_top) {}
    menu "$top.m49" \
        -activebackground $vTcl(actual_gui_menu_analog) \
        -activeforeground #000000 -background $vTcl(actual_gui_menu_bg) \
        -font "TkMenuFont" -foreground $vTcl(actual_gui_menu_fg) -tearoff 0 
### SPOT dump_widget_opt A
    canvas "$top.can53" \
        -background #757575 -closeenough 1.0 -height 84 \
        -highlightbackground #a3a3a3 -highlightcolor black \
        -highlightthickness 0 -insertbackground black -relief ridge \
        -selectbackground #c4c4c4 -selectforeground black -width 958 
    vTcl:DefineAlias "$top.can53" "cvsCabecalho" vTcl:WidgetProc "TelaPrincipal" 1
### SPOT dump_widget_opt A
    set site_3_0 $top.can53
    label "$site_3_0.lab54" \
        -activebackground #f9f9f9 -activeforeground SystemButtonText \
        -anchor w -background #757575 -borderwidth 0 -compound left \
        -disabledforeground #000000 \
        -font "-family Arial -size 30 -weight bold -slant roman -underline 0 -overstrike 0" \
        -foreground #ffff80 -highlightbackground $vTcl(actual_gui_bg) \
        -highlightcolor #000000 -text "SISTEMA IIOT" 
    vTcl:DefineAlias "$site_3_0.lab54" "lblTitulo" vTcl:WidgetProc "TelaPrincipal" 1
### SPOT dump_widget_opt A
    label "$site_3_0.lab55" \
        -activebackground #f9f9f9 -activeforeground SystemButtonText \
        -anchor w -background #757575 -compound left \
        -disabledforeground #a3a3a3 \
        -font "-family Arial -size 20 -weight bold -slant roman -underline 0 -overstrike 0" \
        -foreground #FFFFFF -highlightbackground $vTcl(actual_gui_bg) \
        -highlightcolor black -text "Aluno: Ubiratan da S.Tavares" 
    vTcl:DefineAlias "$site_3_0.lab55" "lblNome" vTcl:WidgetProc "TelaPrincipal" 1
### SPOT dump_widget_opt A
    place $site_3_0.lab54 \
        -in $site_3_0 -x 0 -relx 0.073 -y 0 -rely 0.238 -width 0 \
        -relwidth 0.297 -height 0 -relheight 0.643 -anchor nw \
        -bordermode ignore 
    place $site_3_0.lab55 \
        -in $site_3_0 -x 0 -relx 0.557 -y 0 -rely 0.488 -width 0 \
        -relwidth 0.422 -height 0 -relheight 0.39 -anchor nw \
        -bordermode ignore 
    canvas "$top.can56" \
        -background #757575 -closeenough 1.0 -height 193 \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -highlightthickness 0 -insertbackground black -relief ridge \
        -selectbackground #c4c4c4 -selectforeground black -width 222 
    vTcl:DefineAlias "$top.can56" "cvsMotor1" vTcl:WidgetProc "TelaPrincipal" 1
### SPOT dump_widget_opt A
    set site_3_0 $top.can56
    label "$site_3_0.lab57" \
        -activebackground #f9f9f9 -activeforeground SystemButtonText \
        -anchor w -background #757575 -borderwidth 0 -compound center \
        -disabledforeground #a3a3a3 \
        -font "-family Arial -size 16 -weight bold -slant roman -underline 0 -overstrike 0" \
        -foreground #ffff80 -highlightbackground $vTcl(actual_gui_bg) \
        -highlightcolor black -text "Motor 1" 
    vTcl:DefineAlias "$site_3_0.lab57" "lblMotor1" vTcl:WidgetProc "TelaPrincipal" 1
### SPOT dump_widget_opt A
    label "$site_3_0.lab58" \
        -activebackground #f9f9f9 -activeforeground SystemButtonText \
        -anchor w -background #757575 -compound left \
        -disabledforeground #a3a3a3 -font "TkDefaultFont" \
        -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -image motor1_png 
    vTcl:DefineAlias "$site_3_0.lab58" "imgMotor1" vTcl:WidgetProc "TelaPrincipal" 1
### SPOT dump_widget_opt A
    place $site_3_0.lab57 \
        -in $site_3_0 -x 0 -relx 0.33 -y 0 -rely 0.073 -width 0 \
        -relwidth 0.423 -height 0 -relheight 0.135 -anchor nw \
        -bordermode ignore 
    place $site_3_0.lab58 \
        -in $site_3_0 -x 0 -relx 0.233 -y 0 -rely 0.259 -width 0 \
        -relwidth 0.558 -height 0 -relheight 0.648 -anchor nw \
        -bordermode ignore 
    canvas "$top.can59" \
        -background #757575 -closeenough 1.0 -height 182 \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -highlightthickness 0 -insertbackground black -relief ridge \
        -selectbackground #c4c4c4 -selectforeground black -width 211 
    vTcl:DefineAlias "$top.can59" "cvsMotor2" vTcl:WidgetProc "TelaPrincipal" 1
### SPOT dump_widget_opt A
    set site_3_0 $top.can59
    label "$site_3_0.lab57" \
        -activebackground #f9f9f9 -activeforeground SystemButtonText \
        -anchor w -background #757575 -borderwidth 0 -compound center \
        -disabledforeground #a3a3a3 \
        -font "-family Arial -size 16 -weight bold -slant roman -underline 0 -overstrike 0" \
        -foreground #ffff80 -highlightbackground $vTcl(actual_gui_bg) \
        -highlightcolor black -text "Motor 2" 
    vTcl:DefineAlias "$site_3_0.lab57" "lblMotor2" vTcl:WidgetProc "TelaPrincipal" 1
### SPOT dump_widget_opt A
    label "$site_3_0.lab58" \
        -activebackground #f9f9f9 -activeforeground SystemButtonText \
        -anchor w -background #757575 -compound left \
        -disabledforeground #a3a3a3 -font "TkDefaultFont" \
        -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -image motor1_png 
    vTcl:DefineAlias "$site_3_0.lab58" "imgMotor2" vTcl:WidgetProc "TelaPrincipal" 1
### SPOT dump_widget_opt A
    place $site_3_0.lab57 \
        -in $site_3_0 -x 0 -relx 0.333 -y 0 -rely 0.055 -width 0 \
        -relwidth 0.514 -height 0 -relheight 0.137 -anchor nw \
        -bordermode ignore 
    place $site_3_0.lab58 \
        -in $site_3_0 -x 0 -relx 0.238 -y 0 -rely 0.275 -width 0 \
        -relwidth 0.619 -height 0 -relheight 0.698 -anchor nw \
        -bordermode ignore 
    canvas "$top.can60" \
        -background #757575 -closeenough 1.0 -height 114 \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -highlightthickness 0 -insertbackground black -relief ridge \
        -selectbackground #c4c4c4 -selectforeground black -width 204 
    vTcl:DefineAlias "$top.can60" "cvsTanque1" vTcl:WidgetProc "TelaPrincipal" 1
### SPOT dump_widget_opt A
    set site_3_0 $top.can60
    label "$site_3_0.lab61" \
        -activebackground #f9f9f9 -activeforeground SystemButtonText \
        -anchor w -background #757575 -compound left \
        -disabledforeground #a3a3a3 \
        -font "-family Arial -size 16 -weight bold -slant roman -underline 0 -overstrike 0" \
        -foreground #ffff80 -highlightbackground $vTcl(actual_gui_bg) \
        -highlightcolor black -text "Tanque 1" 
    vTcl:DefineAlias "$site_3_0.lab61" "lblTanque1" vTcl:WidgetProc "TelaPrincipal" 1
### SPOT dump_widget_opt A
    label "$site_3_0.lab62" \
        -activebackground #f9f9f9 -activeforeground SystemButtonText \
        -anchor w -background #757575 -borderwidth 0 -compound left \
        -disabledforeground #a3a3a3 \
        -font "-family Arial -size 30 -weight bold -slant roman -underline 0 -overstrike 0" \
        -foreground #ffffff -highlightbackground $vTcl(actual_gui_bg) \
        -highlightcolor black -text "66" 
    vTcl:DefineAlias "$site_3_0.lab62" "txtVolTanque1" vTcl:WidgetProc "TelaPrincipal" 1
### SPOT dump_widget_opt A
    label "$site_3_0.lab63" \
        -activebackground #f9f9f9 -activeforeground SystemButtonText \
        -anchor w -background #757575 -borderwidth 0 -compound left \
        -disabledforeground #a3a3a3 \
        -font "-family Arial -size 24 -weight bold -slant roman -underline 0 -overstrike 0" \
        -foreground #ffffff -highlightbackground $vTcl(actual_gui_bg) \
        -highlightcolor black -text "m" 
    vTcl:DefineAlias "$site_3_0.lab63" "txtMetroTanque1" vTcl:WidgetProc "TelaPrincipal" 1
### SPOT dump_widget_opt A
    label "$site_3_0.lab64" \
        -activebackground #f9f9f9 -activeforeground SystemButtonText \
        -anchor w -background #757575 -borderwidth 0 -compound left \
        -disabledforeground #a3a3a3 \
        -font "-family Arial -size 24 -weight bold -slant roman -underline 0 -overstrike 0" \
        -foreground #ffffff -highlightbackground $vTcl(actual_gui_bg) \
        -highlightcolor black -text "3" 
    vTcl:DefineAlias "$site_3_0.lab64" "txtCuboTanque1" vTcl:WidgetProc "TelaPrincipal" 1
### SPOT dump_widget_opt A
    place $site_3_0.lab61 \
        -in $site_3_0 -x 0 -relx 0.234 -y 0 -rely 0.07 -width 0 \
        -relwidth 0.533 -height 0 -relheight 0.217 -anchor nw \
        -bordermode ignore 
    place $site_3_0.lab62 \
        -in $site_3_0 -x 0 -relx 0.245 -y 0 -rely 0.42 -width 0 \
        -relwidth 0.25 -height 0 -relheight 0.357 -anchor nw \
        -bordermode ignore 
    place $site_3_0.lab63 \
        -in $site_3_0 -x 0 -relx 0.539 -y 0 -rely 0.49 -width 0 \
        -relwidth 0.157 -height 0 -relheight 0.217 -anchor nw \
        -bordermode ignore 
    place $site_3_0.lab64 \
        -in $site_3_0 -x 0 -relx 0.686 -y 0 -rely 0.35 -width 0 \
        -relwidth 0.157 -height 0 -relheight 0.217 -anchor nw \
        -bordermode ignore 
    canvas "$top.can65" \
        -background #757575 -closeenough 1.0 -height 114 \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -highlightthickness 0 -insertbackground black -relief ridge \
        -selectbackground #c4c4c4 -selectforeground black -width 202 
    vTcl:DefineAlias "$top.can65" "cvsTanque2" vTcl:WidgetProc "TelaPrincipal" 1
### SPOT dump_widget_opt A
    set site_3_0 $top.can65
    label "$site_3_0.lab61" \
        -activebackground #f9f9f9 -activeforeground SystemButtonText \
        -anchor w -background #757575 -compound left \
        -disabledforeground #a3a3a3 \
        -font "-family Arial -size 16 -weight bold -slant roman -underline 0 -overstrike 0" \
        -foreground #ffff80 -highlightbackground $vTcl(actual_gui_bg) \
        -highlightcolor black -text "Tanque 2" 
    vTcl:DefineAlias "$site_3_0.lab61" "lblTanque2" vTcl:WidgetProc "TelaPrincipal" 1
### SPOT dump_widget_opt A
    label "$site_3_0.lab62" \
        -activebackground #f9f9f9 -activeforeground SystemButtonText \
        -anchor w -background #757575 -borderwidth 0 -compound left \
        -disabledforeground #a3a3a3 \
        -font "-family Arial -size 30 -weight bold -slant roman -underline 0 -overstrike 0" \
        -foreground #ffffff -highlightbackground $vTcl(actual_gui_bg) \
        -highlightcolor black -text "95" 
    vTcl:DefineAlias "$site_3_0.lab62" "txtVolTanque2" vTcl:WidgetProc "TelaPrincipal" 1
### SPOT dump_widget_opt A
    label "$site_3_0.lab63" \
        -activebackground #f9f9f9 -activeforeground SystemButtonText \
        -anchor w -background #757575 -borderwidth 0 -compound left \
        -disabledforeground #a3a3a3 \
        -font "-family Arial -size 24 -weight bold -slant roman -underline 0 -overstrike 0" \
        -foreground #ffffff -highlightbackground $vTcl(actual_gui_bg) \
        -highlightcolor black -text "m" 
    vTcl:DefineAlias "$site_3_0.lab63" "txtMetroTanque2" vTcl:WidgetProc "TelaPrincipal" 1
### SPOT dump_widget_opt A
    label "$site_3_0.lab64" \
        -activebackground #f9f9f9 -activeforeground SystemButtonText \
        -anchor w -background #757575 -borderwidth 0 -compound left \
        -disabledforeground #a3a3a3 \
        -font "-family Arial -size 24 -weight bold -slant roman -underline 0 -overstrike 0" \
        -foreground #ffffff -highlightbackground $vTcl(actual_gui_bg) \
        -highlightcolor black -text "3" 
    vTcl:DefineAlias "$site_3_0.lab64" "txtCuboTanque2" vTcl:WidgetProc "TelaPrincipal" 1
### SPOT dump_widget_opt A
    place $site_3_0.lab61 \
        -in $site_3_0 -x 0 -relx 0.233 -y 0 -rely 0.07 -width 0 \
        -relwidth 0.535 -height 0 -relheight 0.217 -anchor nw \
        -bordermode ignore 
    place $site_3_0.lab62 \
        -in $site_3_0 -x 0 -relx 0.248 -y 0 -rely 0.42 -width 0 \
        -relwidth 0.252 -height 0 -relheight 0.357 -anchor nw \
        -bordermode ignore 
    place $site_3_0.lab63 \
        -in $site_3_0 -x 0 -relx 0.545 -y 0 -rely 0.49 -width 0 \
        -relwidth 0.158 -height 0 -relheight 0.217 -anchor nw \
        -bordermode ignore 
    place $site_3_0.lab64 \
        -in $site_3_0 -x 0 -relx 0.654 -y 0 -rely 0.35 -width 0 \
        -relwidth 0.159 -height 0 -relheight 0.217 -anchor nw \
        -bordermode ignore 
    canvas "$top.can66" \
        -background #757575 -closeenough 1.0 -height 114 \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -highlightthickness 0 -insertbackground black -relief ridge \
        -selectbackground #c4c4c4 -selectforeground black -width 172 
    vTcl:DefineAlias "$top.can66" "cvsBotoes" vTcl:WidgetProc "TelaPrincipal" 1
### SPOT dump_widget_opt A
    set site_3_0 $top.can66
    button "$site_3_0.but67" \
        -activebackground $vTcl(analog_color_m) -activeforeground black \
        -background $vTcl(actual_gui_bg) -compound left \
        -disabledforeground #a3a3a3 \
        -font "-family Arial -size 12 -weight bold -slant roman -underline 0 -overstrike 0" \
        -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -pady 0 -text "Config. Alerta" 
    vTcl:DefineAlias "$site_3_0.but67" "btnAlerta" vTcl:WidgetProc "TelaPrincipal" 1
### SPOT dump_widget_opt A
    bind $site_3_0.but67 <Button-1> {
        lambda e: alertar(e)
    }
    button "$site_3_0.but69" \
        -activebackground $vTcl(analog_color_m) -activeforeground black \
        -background $vTcl(actual_gui_bg) -compound left \
        -disabledforeground #a3a3a3 \
        -font "-family Arial -size 12 -weight bold -slant roman -underline 0 -overstrike 0" \
        -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -pady 0 -text "Gráficos" 
    vTcl:DefineAlias "$site_3_0.but69" "btnGrafico" vTcl:WidgetProc "TelaPrincipal" 1
### SPOT dump_widget_opt A
    bind $site_3_0.but69 <Button-1> {
        lambda e: plotar(e)
    }
    place $site_3_0.but67 \
        -in $site_3_0 -x 0 -relx 0.152 -y 0 -rely 0.175 -width 134 \
        -relwidth 0 -height 34 -relheight 0 -anchor nw -bordermode ignore 
    place $site_3_0.but69 \
        -in $site_3_0 -x 0 -relx 0.152 -y 0 -rely 0.614 -width 137 \
        -relwidth 0 -height 34 -relheight 0 -anchor nw -bordermode ignore 
    label "$top.lab70" \
        -activebackground #f9f9f9 -activeforeground SystemButtonText \
        -anchor w -background #303030 -compound left \
        -disabledforeground #a3a3a3 -font "TkDefaultFont" \
        -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -image puc2_png 
    vTcl:DefineAlias "$top.lab70" "imgInstituicao" vTcl:WidgetProc "TelaPrincipal" 1
### SPOT dump_widget_opt A
    label "$top.lab71" \
        -activebackground #f9f9f9 -activeforeground SystemButtonText \
        -anchor w -background #303030 -compound left \
        -disabledforeground #a3a3a3 \
        -font "-family Arial -size 20 -weight bold -slant roman -underline 0 -overstrike 0" \
        -foreground #FFFFFF -highlightbackground $vTcl(actual_gui_bg) \
        -highlightcolor black -text "Disciplina: PDI" 
    vTcl:DefineAlias "$top.lab71" "lblDisciplina" vTcl:WidgetProc "TelaPrincipal" 1
### SPOT dump_widget_opt A
    canvas "$top.can72" \
        -background #757575 -closeenough 1.0 -height 473 \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -highlightthickness 0 -insertbackground black -relief ridge \
        -selectbackground #c4c4c4 -selectforeground black -width 515 
    vTcl:DefineAlias "$top.can72" "cvcTanques" vTcl:WidgetProc "TelaPrincipal" 1
### SPOT dump_widget_opt A
    set site_3_0 $top.can72
    canvas "$site_3_0.can75" \
        -background #0000ff -closeenough 1.0 -height 143 \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -highlightthickness 0 -insertbackground black \
        -selectbackground #000000 -selectforeground #ffffff -width 114 
    vTcl:DefineAlias "$site_3_0.can75" "cvcRetanguloAzul" vTcl:WidgetProc "TelaPrincipal" 1
### SPOT dump_widget_opt A
    canvas "$site_3_0.can76" \
        -background #ffffff -closeenough 1.0 -height 143 \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -highlightthickness 0 -insertbackground black \
        -selectbackground #000000 -selectforeground black -width 103 
    vTcl:DefineAlias "$site_3_0.can76" "cvcRetanguloBranco" vTcl:WidgetProc "TelaPrincipal" 1
### SPOT dump_widget_opt A
    label "$site_3_0.lab77" \
        -activebackground #f9f9f9 -activeforeground SystemButtonText \
        -anchor w -background #757575 -borderwidth 0 -compound left \
        -disabledforeground #a3a3a3 -font "TkDefaultFont" \
        -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -image tanques2_png 
    vTcl:DefineAlias "$site_3_0.lab77" "imgTanques" vTcl:WidgetProc "TelaPrincipal" 1
### SPOT dump_widget_opt A
    place $site_3_0.can75 \
        -in $site_3_0 -x 0 -relx 0.313 -y 0 -rely 0.295 -width 0 \
        -relwidth 0.178 -height 0 -relheight 0.325 -anchor nw \
        -bordermode ignore 
    place $site_3_0.can76 \
        -in $site_3_0 -x 0 -relx 0.548 -y 0 -rely 0.295 -width 0 \
        -relwidth 0.161 -height 0 -relheight 0.325 -anchor nw \
        -bordermode ignore 
    place $site_3_0.lab77 \
        -in $site_3_0 -x 0 -relx 0.172 -y 0 -rely 0.068 -width 0 \
        -relwidth 0.773 -height 0 -relheight 0.911 -anchor nw \
        -bordermode ignore 
    ###################
    # SETTING GEOMETRY
    ###################
    place $top.can53 \
        -in $top -x 0 -relx 0.039 -y 0 -rely 0.035 -width 0 -relwidth 0.932 \
        -height 0 -relheight 0.096 -anchor nw -bordermode ignore 
    place $top.can56 \
        -in $top -x 0 -relx 0.763 -y 0 -rely 0.187 -width 0 -relwidth 0.211 \
        -height 0 -relheight 0.226 -anchor nw -bordermode ignore 
    place $top.can59 \
        -in $top -x 0 -relx 0.763 -y 0 -rely 0.492 -width 0 -relwidth 0.206 \
        -height 0 -relheight 0.213 -anchor nw -bordermode ignore 
    place $top.can60 \
        -in $top -x 0 -relx 0.045 -y 0 -rely 0.781 -width 0 -relwidth 0.228 \
        -height 0 -relheight 0.133 -anchor nw -bordermode ignore 
    place $top.can65 \
        -in $top -x 0 -relx 0.302 -y 0 -rely 0.781 -width 0 -relwidth 0.226 \
        -height 0 -relheight 0.133 -anchor nw -bordermode ignore 
    place $top.can66 \
        -in $top -x 0 -relx 0.56 -y 0 -rely 0.781 -width 0 -relwidth 0.193 \
        -height 0 -relheight 0.133 -anchor nw -bordermode ignore 
    place $top.lab70 \
        -in $top -x 0 -relx 0.841 -y 0 -rely 0.738 -width 0 -relwidth 0.165 \
        -height 0 -relheight 0.204 -anchor nw -bordermode ignore 
    place $top.lab71 \
        -in $top -x 0 -relx 0.763 -y 0 -rely 0.948 -width 0 -relwidth 0.202 \
        -height 0 -relheight 0.034 -anchor nw -bordermode ignore 
    place $top.can72 \
        -in $top -x 0 -relx 0.035 -y 0 -rely 0.187 -width 0 -relwidth 0.626 \
        -height 0 -relheight 0.515 -anchor nw -bordermode ignore 

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

