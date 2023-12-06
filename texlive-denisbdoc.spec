Name:		texlive-denisbdoc
Version:	66137
Release:	1
Summary:	A personal dirty package for documenting packages
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/denisbdoc
License:	lppl1.3c
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/denisbdoc.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/denisbdoc.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/denisbdoc.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
A personal dirty package for documenting packages.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/denisbdoc
%{_texmfdistdir}/tex/latex/denisbdoc
%doc %{_texmfdistdir}/doc/latex/denisbdoc

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
