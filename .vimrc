let mapleader=" "
noremap J 5j
noremap K 5k
noremap <LEADER><CR> :nohlsearch<CR>
map s <nop> 
map S :w<CR>
map Q :q<CR>
map R :source $MYVIMRC<CR>



set scrolloff=5
map <LEADER>sc :set spell!<CR>


"split screen"
map sl :set splitright<CR>:vsplit<CR>
map sh :set nosplitright<CR>:vsplit<CR>
map sk :set nosplitbelow<CR>:split<CR>
map sj :set splitbelow<CR>:split<CR>

map <LEADER>k <C-w>l

"忽略大小写"
set ignorecase
set smartcase
"大写"
inoremap <C-u> <esc>gUiwea

"显示行号"
set number
set relativenumber
"突出显示当前行,列"
set cursorline
set cursorcolumn
"语法高亮"
syntax on
set hlsearch
set incsearch
exec "nohlsearch"
"设置tab长度"
set tabstop=4
set shiftwidth=4
"显示匹配的括号"
set showmatch
"启用鼠标"
set mouse=a
set wrap
set wildmenu

set nocompatible
filetype off
set rtp+=~/.vim/bundle/Vundle.vim
call vundle#begin()
Plugin 'VundleVim/Vundle.vim'
Plugin 'Valloric/YouCompleteMe'
Plugin 'Lokaltog/vim-powerline'
Plugin 'scrooloose/nerdtree'
Plugin 'Yggdroot/indentLine'
Plugin 'davidhalter/jedi-vim'
"缩进指示线"
"let g:indentLine_char='┆'
"let g:indentLine_enabled = 1

call vundle#end()
filetype plugin indent on

"===
"===NERDTree
"===
map tt :NERDTreeToggle<CR>
let g:ycm_use_clangd = 0

if has('python3')
let g:loaded_youcomplete = 1
let g:jedi#force_py_version = 3
let g:pymode_python = 'python3'
endif


