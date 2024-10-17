
Name: 		whizzytex
Version: 	1.5.0
Release: 	1
License: 	LGPL
Summary:	An Emacs minor mode for incremental viewing of LaTeX documents
Group:		Publishing
URL:		https://cristal.inria.fr/whizzytex
Source:		http://cristal.inria.fr/whizzytex/%{name}-%{version}.tgz
BuildRequires: 	emacs-bin
Requires: 	emacs-bin
Requires: 	tetex-latex
BuildArch: 	noarch


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



%changelog
* Wed Sep 09 2009 Thierry Vignaud <tvignaud@mandriva.com> 1.3.1-5mdv2010.0
+ Revision: 434749
- rebuild

* Sun Aug 03 2008 Thierry Vignaud <tvignaud@mandriva.com> 1.3.1-4mdv2009.0
+ Revision: 261982
- rebuild

* Wed Jul 30 2008 Thierry Vignaud <tvignaud@mandriva.com> 1.3.1-3mdv2009.0
+ Revision: 255985
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Mon Dec 10 2007 Guillaume Rousse <guillomovitch@mandriva.org> 1.3.1-1mdv2008.1
+ Revision: 116908
- update to new version 1.3.1
- import whizzytex


* Thu Aug 31 2006 Guillaume Rousse <guillomovitch@mandriva.org> 1.3.0-2mdv2007.0
- Rebuild

* Fri Jan 20 2006 Guillaume Rousse <guillomovitch@mandriva.org> 1.3.0-1mdk
- New release 1.3.0
- fix url

* Wed Dec 28 2005 Guillaume Rousse <guillomovitch@mandriva.org> 1.2.3-2mdk
-fix buildrequires 

* Fri Jul 01 2005 Guillaume Rousse <guillomovitch@mandriva.org> 1.2.3-1mdk 
- new release
- fix initex issue
- fix some perms in examples

* Mon Apr 25 2005 Guillaume Rousse <guillomovitch@mandriva.org> 1.2.2-1mdk
- New release 1.2.2
- spec cleanup

* Mon Nov 22 2004 Guillaume Rousse <guillomovitch@mandrake.org> 1.2.1-1mdk 
- new version
- rpmbuildupdate aware

* Fri Jul 02 2004 Guillaume Rousse <guillomovitch@mandrake.org> 1.1.3-2mdk 
- remove useless provide

* Fri Apr 16 2004 Guillaume Rousse <guillomovitch@mandrake.org> 1.1.3-1mdk
- first mdk release
