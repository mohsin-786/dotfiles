#               *Style-1) change_style   ;;
#				*Style-2) change_style   ;;
#				*Style-3) change_style   ;;
#				*Style-4) change_style   ;;
#				*Style-5) change_style   ;;
#				*Style-6) change_style   ;;
#				*Style-7) change_style   ;;
#				*Style-8) change_style   ;;
#				*Style-9) change_style   ;;
#				*Style-10) change_style   ;;
#				*Style-11) change_style   ;;
#				*Style-12) change_style   ;;

import os
import re
import socket
import subprocess
import psutil

from typing import List  # noqa: F401zzz

from libqtile import bar, layout, widget, hook
from libqtile.config import (KeyChord,Key,Screen,Group,Drag,Click,ScratchPad,DropDown,Match,)
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal
from libqtile.command import lazy
from libqtile import qtile


# AUTOSTART
@hook.subscribe.startup_once
def autostart():
    home = os.path.expanduser('~/.config/qtile/autostart.sh')
    subprocess.Popen([home])


# KEY BINDINGS
mod = "mod4"              # Sets mod key to SUPER/WINDOWS
myTerm = "alacritty"      # My terminal of choice
myBrowser = "brave" # My browser of choice
myLauncher = "rofi -no-lazy-grab -show drun"
myFile = "thunar"
myLock = "betterlockscreen -l"

keys = [
         ### The essentials
         Key([mod], "Return",
             lazy.spawn(myTerm),
             desc='Launches My Terminal'
             ),
         Key([mod] , "o",
             lazy.spawn(myLauncher),
             desc='Run Launcher'
             ),
         Key([mod], "b",
             lazy.spawn(myBrowser),
             desc='Brave'
             ),
         Key([mod], "Tab",
             lazy.next_layout(),
             desc='Toggle through layouts'
             ),
         Key([mod] , "q",
             lazy.window.kill(),
             desc='Kill active window'
             ),
         Key([mod, "shift"], "r",
             lazy.restart(),
             desc='Restart Qtile'
             ),
         Key([mod, "shift"], "q",
             lazy.shutdown(),
             desc='Shutdown Qtile'
             ),
         Key([mod, "shift"], "Return",
             lazy.spawn(myFile),
             desc='File Manager'
             ),
         ### Switch focus to specific monitor (out of three)
         Key([mod], "w",
             lazy.to_screen(0),
             desc='Keyboard focus to monitor 1'
             ),
         Key([mod], "e",
             lazy.to_screen(1),
             desc='Keyboard focus to monitor 2'
             ),
         Key([mod], "r",
             lazy.to_screen(2),
             desc='Keyboard focus to monitor 3'
             ),
         ### Switch focus of monitors
         Key([mod], "period",
             lazy.next_screen(),
             desc='Move focus to next monitor'
             ),
         Key([mod], "comma",
             lazy.prev_screen(),
             desc='Move focus to prev monitor'
             ),
         ### Treetab controls
          Key([mod, "shift"], "h",
             lazy.layout.move_left(),
             desc='Move up a section in treetab'
             ),
         Key([mod, "shift"], "l",
             lazy.layout.move_right(),
             desc='Move down a section in treetab'
             ),
         ### Window controls
         Key([mod], "j",
             lazy.layout.down(),
             desc='Move focus down in current stack pane'
             ),
         Key([mod], "k",
             lazy.layout.up(),
             desc='Move focus up in current stack pane'
             ),
         Key([mod, "shift"], "j",
             lazy.layout.shuffle_down(),
             lazy.layout.section_down(),
             desc='Move windows down in current stack'
             ),
         Key([mod, "shift"], "k",
             lazy.layout.shuffle_up(),
             lazy.layout.section_up(),
             desc='Move windows up in current stack'
             ),
         Key([mod], "Right",
             lazy.layout.shrink(),
             lazy.layout.decrease_nmaster(),
             desc='Shrink window (MonadTall), decrease number in master pane (Tile)'
             ),
         Key([mod], "Left",
             lazy.layout.grow(),
             lazy.layout.increase_nmaster(),
             desc='Expand window (MonadTall), increase number in master pane (Tile)'
             ),
         Key([mod], "n",
             lazy.layout.normalize(),
             desc='normalize window size ratios'
             ),
             Key([mod], "l",
             lazy.spawn(myLock),
             desc='betterlockscreen'
             ),
         Key([mod], "m",
             lazy.layout.maximize(),
             desc='toggle window between minimum and maximum sizes'
             ),
         Key([mod, "shift"], "f",
             lazy.window.toggle_floating(),
             desc='toggle floating'
             ),
         Key([mod], "f",
             lazy.window.toggle_fullscreen(),
             desc='toggle fullscreen'
             ),
         ### Stack controls
         Key([mod, "shift"], "Tab",
             lazy.layout.rotate(),
             lazy.layout.flip(),
             desc='Switch which side main pane occupies (XmonadTall)'
             ),
          Key([mod], "space",
             lazy.layout.next(),
             desc='Switch window focus to other pane(s) of stack'
             ),
         Key([mod, "shift"], "space",
             lazy.layout.toggle_split(),
             desc='Toggle between split and unsplit sides of stack'
             ),
        
   
# Media Keys
    Key(
        [],
        "XF86AudioLowerVolume",
        lazy.spawn("pamixer -d 5 | vol.sh"),
        desc="Lower volume",
    ),
    Key(
        [],
        "XF86AudioRaiseVolume",
        lazy.spawn("pamixer -i 5 | vol.sh"),
        desc="Raise volume",
    ),
    Key(
        [],
        "XF86AudioMute",
        lazy.spawn("pamixer -t | vol.sh"),
        desc="Mute volume",
    ),
    Key(
        [],
        "XF86AudioPlay",
        lazy.spawn("playerctl play-pause"),
        desc="Play or pause music",
    ),
    Key([], "XF86AudioNext", lazy.spawn("playerctl next"), desc="Next track"),
    Key([], "XF86AudioPrev", lazy.spawn("playerctl previous"), desc="Previous track"),
    Key([], "XF86AudioStop", lazy.spawn("playerctl stop"), desc="Stop track"),
    # Screen brightness
    Key(
        [],
        "XF86MonBrightnessUp",
        lazy.spawn("brightnessctl set +5%"),
        desc="Raise screen brightness",
    ),
    Key(
        [],
        "XF86MonBrightnessDown",
        lazy.spawn("brightnessctl set 5%-"),
        desc="Lower screen brightness",
    ),
    # Take a screenshot
    Key([], "Print", lazy.spawn("flameshot gui"), desc="Take a screenshot"),
    
    
]

# COLORS FOR THE BAR
colors = [
    ["#ecf0c1", "#ecf0c1"],  # ACTIVE WORKSPACES 0
    ["#686f9a", "#686f9a"],  # INACTIVE WORKSPACES 1
    ["#16172d", "#16172d"],  # background lighter 2
    ["#e33400", "#e33400"],  # red 3
    ["#5ccc96", "#5ccc96"],  # green 4
    ["#b3a1e6", "#b3a1e6"],  # yellow 5
    ["#00a3cc", "#00a3cc"],  # blue 6
    ["#f2ce00", "#f2ce00"],  # magenta 7
    ["#7a5ccc", "#7a5ccc"],  # cyan 8
    ["#686f9a", "#686f9a"],  # white 9
    ["#f0f1ce", "#f0f1ce"],  # grey 10
    ["#d08770", "#d08770"],  # orange 11
    ["#1b1c36", "#1b1c36"],  # super cyan12
    ["#0f111b", "#0f111b"],  # super blue 13
    ["#0e131a", "#0e131a"],  # super dark background 14
]



# WORKSPACES
groups = [Group(i) for i in ["", "", "", "", "", "", "", "", "", ""]]
group_hotkeys = "1234567890"

for g, k in zip(groups, group_hotkeys):
    keys.extend(
        [
            # mod1 + letter of group = switch to group
            Key(
                [mod],
                k,
                lazy.group[g.name].toscreen(),
                desc=f"Switch to group {g.name}",
            ),
            # mod1 + shift + letter of group = switch to & move focused window to group
            Key(
                [mod, "shift"],
                k,
                lazy.window.togroup(g.name, switch_group=False),
                desc=f"Switch to & move focused window to group {g.name}",
            ),
            # Or, use below if you prefer not to switch to that group.
            # # mod1 + shift + letter of group = move focused window to group
            # Key([mod, "shift"], i.name, lazy.window.togroup(i.name),
            #     desc="move focused window to group {}".format(i.name)),
        ]
    )

    
group_box_settings = {
    "padding" : 5,
                    "borderwidth" : 3,
                    "fontsize": 20,
                    "active" : colors[0],
                    "inactive" : colors[1],
                    "disable_drag" : True,
                    "rounded" : True,
                    "margin_y" : 3,
                    "margin_x" : 2,
                    "padding_y" : 5,
                    "padding_x" : 4,
                    #hide_unused" :True,
                    "highlight_color" : colors[9],
                    "highlight_method" : "block",
                    "this_current_screen_border" : colors[11],
                    "this_screen_border" : colors [1],
                    "other_current_screen_border" : colors[1],
                    "other_screen_border" : colors[1],
                    "foreground" : colors[4],
                    "background" : colors[12],
}


layout_theme = {
    "border_width": 3,
    "margin": 9,
    "border_focus": "5ccc96",
    "border_normal": "#FF0000",
    "font": "FiraCode Nerd Font",
    "grow_amount": 2,
}

layouts = [
    #layout.Max(**layout_theme),
    layout.MonadTall(**layout_theme),
    layout.Bsp(**layout_theme),
    layout.RatioTile(**layout_theme),
    #layout.Stack(num_stacks=2, **layout_theme),
    layout.Floating(**layout_theme, fullscreen_border_width=3, max_border_width=3),
]



#group_box_settings = {
#    "padding" : 5,
 #                   "borderwidth" : 3,
  #                  "fontsize": 20,
   #                 "active" : colors[0],
    #                "inactive" : colors[1],
     #               "disable_drag" : True,
      #              "rounded" : True,
       #             "margin_y" : 3,
        #            "margin_x" : 2,
         #           "padding_y" : 5,
          #          "padding_x" : 4,
           #         #hide_unused" :True,
            #        "highlight_color" : colors[9],
             #       "highlight_method" : "block",
              #      "this_current_screen_border" : colors[11],
               #     "this_screen_border" : colors [1],
                #    "other_current_screen_border" : colors[1],
                 #   "other_screen_border" : colors[1],
                  #  "foreground" : colors[4],
                   # "background" : colors[12],
#}

widget_defaults = dict(
    font="novamono for powerline bold", fontsize=11, padding=3, background=colors[14]
)
extension_defaults = widget_defaults.copy()

def open_pavu():
    qtile.cmd_spawn("pavucontrol")

def open_jgmenu():
    qtile.cmd_spawn("jgmenu_run")

def open_calendar():
    qtile.cmd_spawn("gsimplecal")

def open_pacman():
    qtile.cmd_spawn("alacritty -e sudo pacman -Syu")
    
def open_mem():
    qtile.cmd_spawn("alacritty -e htop")
    
 
    
screens = [
    Screen(
        top=bar.Bar(
            [
                widget.Sep(
                        linewidth = 1,
                        padding = 10,
                        foreground = colors[12],
                        background = colors[12]
                        ),
                widget.CurrentLayoutIcon(
				padding=1,
				scale=0.8,
				background=colors[11],
				custom_icon_paths=["/home/aspect/.config/qtile/icons/"],
        ),
				widget.CurrentLayout(background=colors[12]),
				widget.TextBox(
                       text = "",
                       font = "Iosevka_Nerd_Font",
                       fontsize = 23,
                       background = colors[7],
                       foreground = colors[12],
                       padding = 0
                       ),
                widget.GroupBox(
					   **group_box_settings
        ),
                widget.TextBox(
                       text = "",
                       font = "Iosevka_Nerd_Font",
                       fontsize = 24,
                       background = colors[13],
                       foreground = colors[12],
                       padding = 0
                       ),
                widget.TaskList(
                       font="feather",
                       borderwidth=2,
                       padding=3,
                       margin=3,
                       highlight_method=colors[3],
                       border=colors[4],
                       background=colors[13],
                       ),
                widget.Spacer(
                       background=colors[13],
                       ),
                widget.TextBox(
                       text = "",
                       font = "Iosevka_Nerd_Font",
                       fontsize = 23,
                       background = colors[13],
                       foreground = colors[12],
                       padding = 0
                       ),
                widget.TextBox(
                       text = "",
                       font = "Iosevka_Nerd_Font",
                       fontsize = 23,
                       background = colors[12],
                       foreground = colors[7],
                       padding = 0
                       ),
                        widget.Battery(
						format="{char} {percent:2.0%}",
						charge_char="",
						discharge_char="",
						full_char="",
						unknown_char="",
						empty_char="",
						show_short_text=False,
						background=colors[7],
						fontsize=14,
						foreground=colors[13]
						),
						widget.Volume(
						fmt=" 墳 {}",
						mute_command="pamixer -t",
						volume_down_command="pamixer -d 5",
						volume_up_command="pamixer -i 5",
						volume_app="pavucontrol",
						mouse_callbacks={"Button1": open_pavu},
						fontsize=15,
						scroll=False,
						background=colors[7],
						foreground=colors[13]
						),
                widget.TextBox(
                       text = "",
                       font = "Iosevka_Nerd_Font",
                       fontsize = 23,
                       background = colors[7],
                       foreground = colors[12],
                       padding = 0
                       ),
                widget.TextBox(
                       text = "",
                       font = "Iosevka_Nerd_Font",
                       fontsize = 23,
                       background = colors[12],
                       foreground = colors[6],
                       padding = 0
                       ),
                widget.TextBox(
                    text=" ",
                    foreground=colors[13],
                    background=colors[6],
                    font = "feather",
                    fontsize=17,
                    padding=0,
                ),
                widget.ThermalSensor(
                         foreground = colors[13],
                         foreground_alert = colors[13],
                         background = colors[6],
                         fontsize=14,
                         metric = True,
                         padding = 4,
                         threshold = 80
                         ),
                widget.TextBox(
                       text = "",
                       font = "Iosevka_Nerd_Font",
                       fontsize = 23,
                       background = colors[6],
                       foreground = colors[12],
                       padding = 0
                       ),
                widget.TextBox(
                       text = "",
                       font = "Iosevka_Nerd_Font",
                       fontsize = 23,
                       background = colors[12],
                       foreground = colors[5],
                       padding = 0
                       ),
                widget.TextBox(
                       text = " ",
                       font = "feather",
                       fontsize = 17,
                       background = colors[5],
                       foreground = colors[13],
                       padding = 0,
                       ),
                widget.Memory(
                        background=colors[5],
                        foreground=colors[13],
                        fontsize=14,
                        mouse_callbacks={"Button1" : open_mem},
                        format='{MemUsed: .0f} MB ',
                        ),
                widget.TextBox(
                       text = "",
                       font = "Iosevka_Nerd_Font",
                       fontsize = 23,
                       background = colors[5],
                       foreground = colors[12],
                       padding = 0
                       ),
                widget.TextBox(
                       text = "",
                       font = "Iosevka_Nerd_Font",
                       fontsize = 23,
                       background = colors[12],
                       foreground = colors[4],
                       padding = 0
                       ),
                widget.TextBox(
                       text = "  ",
                       font = "feather",
                       fontsize = 17,
                       foreground = colors[13],
                       background = colors[4],
                       padding = 0
                       ),
                       
                widget.CPU(
                format='{freq_current}GHz',
                foreground=colors[13],
                background=colors[4],
                fontsize=14
                ),
                widget.TextBox(
                       text = "",
                       font = "Iosevka_Nerd_Font",
                       fontsize = 23,
                       background = colors[4],
                       foreground = colors[12],
                       padding = 0
                       ),
                widget.TextBox(
                       text = "",
                       font = "Iosevka_Nerd_Font",
                       fontsize = 23,
                       background = colors[12],
                       foreground = colors[7],
                       padding = 0
                       ),
                widget.TextBox(
                    text="",
                    foreground=colors[13],
                    background=colors[7],
                    font = "feather",
                    fontsize=17,
                    padding=0,
                ),
                widget.Net(
                         foreground = colors[13],
                         background = colors[7],
                         fontsize = 14,
                         format = "\u2193 {down} \u2191 {up}",
						 interface= "wlp2s0",
						 update_interval= 2
                         ),
                widget.TextBox(
                       text = "",
                       font = "Iosevka_Nerd_Font",
                       fontsize = 23,
                       background = colors[7],
                       foreground = colors[12],
                       padding = 0
                       ),
                widget.TextBox(
                       text = "",
                       font = "Iosevka_Nerd_Font",
                       fontsize = 23,
                       background = colors[12],
                       foreground = colors[9],
                       padding = 0
                       ),
                widget.Systray(
                background = colors[9],
                ),
                widget.TextBox(
                       text = "",
                       font = "Iosevka_Nerd_Font",
                       fontsize = 23,
                       background = colors[9],
                       foreground = colors[12],
                       padding = 0
                       ),
                widget.TextBox(
                       text = "",
                       font = "Iosevka_Nerd_Font",
                       fontsize = 23,
                       background = colors[12],
                       foreground = colors[3],
                       padding = 0
                       ),
                       widget.TextBox(
                       text = " ",
                       font = "feather",
                       fontsize = 18,
                       foreground = colors[13],
                       background = colors[3],
                       padding = 0
                       ),
                
                widget.Clock(
                       background = colors[3],
                       foreground = colors[13],
                       fontsize=14,
                       format="  %a %d %b %Y, %I:%M %p"
                ),
                widget.TextBox(
                       text = "",
                       font = "Iosevka_Nerd_Font",
                       fontsize = 23,
                       background = colors[3],
                       foreground = colors[12],
                       padding = 0
                       ),
                widget.Sep(
                        linewidth = 1,
                        padding = 10,
                        foreground = colors[12],
                        background = colors[12]
                        ),
            ],
            30,
            margin=[6, 15, 5, 15],
            border_width= 4,
            border_color= "#b3a1e6",
            opacity= 1.0,
        ),
        bottom=bar.Gap(18),
        left=bar.Gap(18),
        right=bar.Gap(18),
    ),
]

# Drag floating layouts.
mouse = [
    Drag(
        [mod],
        "Button1",
        lazy.window.set_position_floating(),
        start=lazy.window.get_position(),
    ),
    Drag(
        [mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()
    ),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
    ]
)
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# When using the Wayland backend, this can be used to configure input devices.
wl_input_rules = None

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"
