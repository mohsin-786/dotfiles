static const char norm_fg[] = "#a3d8c1";
static const char norm_bg[] = "#01080F";
static const char norm_border[] = "#729787";

static const char sel_fg[] = "#a3d8c1";
static const char sel_bg[] = "#346C69";
static const char sel_border[] = "#a3d8c1";

static const char urg_fg[] = "#a3d8c1";
static const char urg_bg[] = "#2B635D";
static const char urg_border[] = "#2B635D";

static const char *colors[][3]      = {
    /*               fg           bg         border                         */
    [SchemeNorm] = { norm_fg,     norm_bg,   norm_border }, // unfocused wins
    [SchemeSel]  = { sel_fg,      sel_bg,    sel_border },  // the focused win
    [SchemeUrg] =  { urg_fg,      urg_bg,    urg_border },
};
