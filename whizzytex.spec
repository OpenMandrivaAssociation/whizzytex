%define name	whizzytex
%define version 1.3.1
%define release %mkrel 5

Name: 		%{name}
Version: 	%{version}
Release: 	%{release}
License: 	LGPL
Summary:	An Emacs minor mode for incremental viewing of LaTeX documents
Group:		Publishing
URL:		http://cristal.inria.fr/whizzytex
Source:		http://cristal.inria.fr/whizzytex/%{name}-%{version}.tar.bz2
BuildRequires: 	emacs-bin
Requires: 	emacs-bin
Requires: 	tetex-latex
BuildArch: 	noarch
BuildRoot: 	%{_tmppath}/%{name}-%{version}

%description 
WhizzyTeX provides a minor mode for Emacs or XEmacs, a (bash) shell-script
daemon and some LaTeX macros. It works under Unix with gv and xdvi viewers, but
the Active-DVI viewer will provided much better visual effects and will offer
more functionalities.

%prep
%setup -q
find . -name .*~ -exec rm -f {} \;
rm -rf examples/beamer
rm -f examples/hyperref/main.out
perl -pi -e 's/INITEX=initex/INITEX="pdfetex -ini"/' src/whizzytex
chmod 755 examples/bin/gpic*
chmod 755 examples/gpic/whizzy.sh

%build
emacs -batch -f batch-byte-compile src/whizzytex.el

%install
rm -rf %{buildroot}
install -d -m 755 %{buildroot}%{_bindir}
install -d -m 755 %{buildroot}%{_datadir}/emacs/site-lisp
install -d -m 755 %{buildroot}%{_datadir}/texmf/tex/latex/%{name}
install -m 755 src/whizzytex %{buildroot}%{_bindir}
install -m 644 src/whizzytex.sty %{buildroot}%{_datadir}/texmf/tex/latex/%{name}
install -m 644 src/whizzytex.el* %{buildroot}%{_datadir}/emacs/site-lisp

%clean
rm -rf %{buildroot}

%post -p %{_bindir}/mktexlsr

%postun -p %{_bindir}/mktexlsr

%files
%defattr(-,root,root)
%doc CHANGES COPYING FILES INSTALL GPL VERSION doc examples
%{_bindir}/%{name}
%{_datadir}/texmf/tex/latex/%{name}
%{_datadir}/emacs/site-lisp

