const char *colorname[] = {

  /* 8 normal colors */
  [0] = "#01080F", /* black   */
  [1] = "#2B635D", /* red     */
  [2] = "#346C69", /* green   */
  [3] = "#47776E", /* yellow  */
  [4] = "#229B65", /* blue    */
  [5] = "#528979", /* magenta */
  [6] = "#5F9C89", /* cyan    */
  [7] = "#a3d8c1", /* white   */

  /* 8 bright colors */
  [8]  = "#729787",  /* black   */
  [9]  = "#2B635D",  /* red     */
  [10] = "#346C69", /* green   */
  [11] = "#47776E", /* yellow  */
  [12] = "#229B65", /* blue    */
  [13] = "#528979", /* magenta */
  [14] = "#5F9C89", /* cyan    */
  [15] = "#a3d8c1", /* white   */

  /* special colors */
  [256] = "#01080F", /* background */
  [257] = "#a3d8c1", /* foreground */
  [258] = "#a3d8c1",     /* cursor */
};

/* Default colors (colorname index)
 * foreground, background, cursor */
 unsigned int defaultbg = 0;
 unsigned int defaultfg = 257;
 unsigned int defaultcs = 258;
 unsigned int defaultrcs= 258;
