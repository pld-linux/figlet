%define		major	2
%define		minor	2
Summary:	Awesome ASCII-art banners generator
Summary(pl):	Program do generowania odjazowych napisów ASCII
Name:		figlet
Version:	%{major}.%{minor}
Release:	1
Group:		Applications/Games
Group(de):	Applikationen/Spiele
Group(pl):	Aplikacje/Gry
License:	free
Source0:	ftp://wuarchive.wustl.edu/graphics/graphics/misc/figlet/program/unix/%{name}%{major}%{minor}.tar.gz
Patch0:		%{name}-makefile.patch
URL:		http://st-www.cs.uiuc.edu/~chai/figlet.html
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Program for generating ASCII-art-like banners by using plenty of
fonts. It can be used for generating logos, e-mail signatures, etc.

%description -l pl
Program do generacji napisów ze znaków semigraficznych przy u¿yciu
du¿ego wyboru czcionek. Mo¿e byæ wykorzystany do tworzenia logo,
podpisów do listów e-mail, itp.

%prep
%setup -q -n %{name}%{major}%{minor}
%patch -p1

%build
CFLAGS="%{rpmcflags}" \
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_prefix}/{games,share/games/figlet}
install -d $RPM_BUILD_ROOT%{_mandir}/man6

install figlet $RPM_BUILD_ROOT%{_prefix}/games
install chkfont $RPM_BUILD_ROOT%{_prefix}/games
cp -f fonts/* $RPM_BUILD_ROOT%{_datadir}/games/figlet

gzip -9nf {FTP-NOTE,README,figfont.txt,figlist,figmagic,showfigfonts}
install figlet.6 $RPM_BUILD_ROOT%{_mandir}/man6

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_prefix}/games/*
%doc {FTP-NOTE,README,figfont.txt,figlist,figmagic,showfigfonts}.gz

%{_datadir}/games/figlet
%{_mandir}/man6/figlet.6*
