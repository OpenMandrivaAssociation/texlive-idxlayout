Name:		texlive-idxlayout
Version:	0.4c
Release:	1
Summary:	Configurable index layout, responsive to KOMA-Script and memoir
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/idxlayout
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/idxlayout.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/idxlayout.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/idxlayout.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3
Conflicts:	texlive-source <= 20110705-3

%description
The idxlayout package offers a key-value interface to configure
index layout parameters, e.g. allowing for three-column indexes
or for "parent" items and their affiliated subitems being
typeset as a single paragraph. The package is responsive to the
index-related options and commands of the KOMA-Script and
memoir classes.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/idxlayout/idxlayout.sty
%doc %{_texmfdistdir}/doc/latex/idxlayout/README
%doc %{_texmfdistdir}/doc/latex/idxlayout/idxlayout.pdf
#- source
%doc %{_texmfdistdir}/source/latex/idxlayout/idxlayout.dtx
%doc %{_texmfdistdir}/source/latex/idxlayout/idxlayout.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
