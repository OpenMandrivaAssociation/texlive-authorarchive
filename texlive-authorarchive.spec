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
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This is a LaTeX style for producing author self-archiving copies of
(academic) papers. The following layout-styles are pre-defined: ACM for
the two-column layout used by many ACM conferences IEEE for the two-
column layout used by many IEEE conferences LNCS for the LNCS layout (as
used by Springer) LNI for the Lecture Notes in Informatics, published by
the GI ENTCS for the Elsevier ENTCS layout

