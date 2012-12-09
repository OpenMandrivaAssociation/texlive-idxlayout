# revision 25821
# category Package
# catalog-ctan /macros/latex/contrib/idxlayout
# catalog-date 2012-04-01 20:39:12 +0200
# catalog-license lppl
# catalog-version 0.4d
Name:		texlive-idxlayout
Version:	0.4d
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
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The idxlayout package offers a key-value interface to configure
index layout parameters, e.g. allowing for three-column indexes
or for "parent" items and their affiliated subitems being
typeset as a single paragraph. The package is responsive to the
index-related options and commands of the KOMA-Script and
memoir classes.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
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


%changelog
* Fri Apr 13 2012 Paulo Andrade <pcpa@mandriva.com.br> 0.4d-1
+ Revision: 790626
- Update to latest release.

* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 0.4c-2
+ Revision: 752685
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 0.4c-1
+ Revision: 718693
- texlive-idxlayout
- texlive-idxlayout
- texlive-idxlayout
- texlive-idxlayout

