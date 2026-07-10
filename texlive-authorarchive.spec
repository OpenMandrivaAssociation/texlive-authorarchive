%global tl_name authorarchive
%global tl_revision 77171

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.3.1
Release:	%{tl_revision}.1
Summary:	Adds self-archiving information to scientific papers
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/authorarchive
License:	lppl1.3c bsd2
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/authorarchive.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/authorarchive.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
Requires(pre):	texlive-tlpkg
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This is a LaTeX style for producing author self-archiving copies of
(academic) papers. The following layout-styles are pre-defined: ACM for
the two-column layout used by many ACM conferences IEEE for the two-
column layout used by many IEEE conferences LNCS for the LNCS layout (as
used by Springer) LNI for the Lecture Notes in Informatics, published by
the GI ENTCS for the Elsevier ENTCS layout

%prep
%setup -q -c -a1
rm -rf tlpkg
if [ -d RELOC ]; then
	cp -a RELOC/. .
	rm -rf RELOC
fi

%build

%install
mkdir -p %{buildroot}%{_datadir}/texmf-dist
# Flat tlnet layout: tex/ doc/ source/ fonts/ ... -> texmf-dist/
if [ -d texmf-dist ]; then
	cp -a texmf-dist/. %{buildroot}%{_datadir}/texmf-dist/
elif [ -d texmf ]; then
	mkdir -p %{buildroot}%{_datadir}/texmf
	cp -a texmf/. %{buildroot}%{_datadir}/texmf/
else
	for d in * .[!.]* ..?*; do
		[ -e "$d" ] || continue
		case "$d" in tlpkg|RELOC) continue ;; esac
		cp -a "$d" %{buildroot}%{_datadir}/texmf-dist/
	done
fi
rm -rf %{buildroot}%{_datadir}/texmf-dist/tlpkg

%files
%dir %{_datadir}/texmf-dist
%dir %{_datadir}/texmf-dist/doc
%dir %{_datadir}/texmf-dist/tex
%dir %{_datadir}/texmf-dist/doc/latex
%dir %{_datadir}/texmf-dist/tex/latex
%dir %{_datadir}/texmf-dist/doc/latex/authorarchive
%dir %{_datadir}/texmf-dist/tex/latex/authorarchive
%dir %{_datadir}/texmf-dist/doc/latex/authorarchive/examples
%dir %{_datadir}/texmf-dist/doc/latex/authorarchive/examples/bib
%doc %{_datadir}/texmf-dist/doc/latex/authorarchive/CHANGELOG.md
%doc %{_datadir}/texmf-dist/doc/latex/authorarchive/LICENSE
%doc %{_datadir}/texmf-dist/doc/latex/authorarchive/README.md
%doc %{_datadir}/texmf-dist/doc/latex/authorarchive/examples/authorarchive.config
%doc %{_datadir}/texmf-dist/doc/latex/authorarchive/examples/bib/brucker-authorarchive-2016.bib
%doc %{_datadir}/texmf-dist/doc/latex/authorarchive/examples/bib/brucker-authorarchive-2016.enw
%doc %{_datadir}/texmf-dist/doc/latex/authorarchive/examples/bib/brucker-authorarchive-2016.ris
%doc %{_datadir}/texmf-dist/doc/latex/authorarchive/examples/bib/brucker-authorarchive-2016.word.xml
%doc %{_datadir}/texmf-dist/doc/latex/authorarchive/examples/brucker-authorarchive-2016-IEEEtran-nourl.pdf
%doc %{_datadir}/texmf-dist/doc/latex/authorarchive/examples/brucker-authorarchive-2016-IEEEtran-nourl.tex
%doc %{_datadir}/texmf-dist/doc/latex/authorarchive/examples/brucker-authorarchive-2016-IEEEtran.pdf
%doc %{_datadir}/texmf-dist/doc/latex/authorarchive/examples/brucker-authorarchive-2016-IEEEtran.tex
%doc %{_datadir}/texmf-dist/doc/latex/authorarchive/examples/brucker-authorarchive-2016-acmart.pdf
%doc %{_datadir}/texmf-dist/doc/latex/authorarchive/examples/brucker-authorarchive-2016-acmart.tex
%doc %{_datadir}/texmf-dist/doc/latex/authorarchive/examples/brucker-authorarchive-2016-entcs.pdf
%doc %{_datadir}/texmf-dist/doc/latex/authorarchive/examples/brucker-authorarchive-2016-entcs.tex
%doc %{_datadir}/texmf-dist/doc/latex/authorarchive/examples/brucker-authorarchive-2016-llncs-a4.pdf
%doc %{_datadir}/texmf-dist/doc/latex/authorarchive/examples/brucker-authorarchive-2016-llncs-a4.tex
%doc %{_datadir}/texmf-dist/doc/latex/authorarchive/examples/brucker-authorarchive-2016-llncs.pdf
%doc %{_datadir}/texmf-dist/doc/latex/authorarchive/examples/brucker-authorarchive-2016-llncs.tex
%doc %{_datadir}/texmf-dist/doc/latex/authorarchive/examples/brucker-authorarchive-2016-lni.pdf
%doc %{_datadir}/texmf-dist/doc/latex/authorarchive/examples/brucker-authorarchive-2016-lni.tex
%doc %{_datadir}/texmf-dist/doc/latex/authorarchive/examples/brucker-authorarchive-2016.pdf
%doc %{_datadir}/texmf-dist/doc/latex/authorarchive/examples/brucker-authorarchive-2016.tex
%{_datadir}/texmf-dist/tex/latex/authorarchive/authorarchive.sty
