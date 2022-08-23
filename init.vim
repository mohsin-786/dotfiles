call plug#begin()
Plug 'SirVer/ultisnips'
Plug 'honza/vim-snippets'
Plug 'dylanaraps/wal.vim'
Plug 'itchyny/lightline.vim'
Plug 'preservim/nerdtree'
Plug 'ryanoasis/vim-devicons'
Plug 'folke/tokyonight.nvim'
call plug#end()

let g:lightline = {
      \ 'colorscheme': 'deus',
      \ }

let g:tokyonight_style = "night"
colorscheme tokyonight
