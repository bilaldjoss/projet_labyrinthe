\documentclass{report}

\setcounter{secnumdepth}{3}
\renewcommand{\thesection}{\Roman{section}} 
\renewcommand{\thesubsection}{\thesection.\Roman{subsection}}
\renewcommand{\thesubsubsection}{\thesubsection.\Roman{subsubsection}}

\makeatletter
\renewcommand{\maketitle}{
\begin{center}

\pagestyle{empty}
\phantom{.}  %necessary to add space on top before the title
\vspace{0.1cm}

{\LARGE \bf \@title\par}
\vspace{1.0cm}

{\normalsize AIT BELKACEM Moncef, AMADI Bilal, LABOURET Lucas}\\[0.5cm]

{\normalsize UE Projet Math-Info ldd-im2 s2}

\vspace{1.5cm}

%if you want something in the bottom of the page just use \vfill before that.

\end{center}
}\makeatother

\usepackage[margin=0.5in]{geometry}
\title{Projet Labyrinthe}
\author{Moncef Karim AIT BELKACEM}

\begin{document}

\maketitle
Projet d'informatique effectue au s2 a l'universite paris saclay.
\section{Sujet}

\section{Étude théorique du problème}
\subsection{Questions}
\section{Modélisation et exploration}
\section{Ouverture}


\end{document}


