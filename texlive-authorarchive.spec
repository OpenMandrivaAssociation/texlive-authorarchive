Name:		texlive-authorarchive
Version:	63146
Release:	1
Summary:	Adds self-archiving information to scientific papers
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/authorarchive
License:	lppl1.3c bsd2
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/authorarchive.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/authorarchive.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This is a LaTeX style for producing author self-archiving
copies of (academic) papers. The following layout-styles are
pre-defined: ACMfor the two-column layout used by many ACM
conferences IEEE for the two-column layout used by many IEEE
conferences LNCS for the LNCS layout (as used by Springer) LNI
for the Lecture Notes in Informatics, published by the GI ENTCS
for the Elsevier ENTCS layout

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/authorarchive
%doc %{_texmfdistdir}/doc/latex/authorarchive

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
