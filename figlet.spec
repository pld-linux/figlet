%define		major	2
%define		minor	2
Summary:	Awesome ASCII-art banners generator.
Summary(pl):	Program do generowania odjazowych napisów ASCII.
Name:		figlet
Version:	%{major}.%{minor}
Release:	1
Group:          Games
Group(pl):      Gry
Copyright:	free
Vendor:		PLD
Distribution:	PLD
Source:		ftp://wuarchive.wustl.edu/graphics/graphics/misc/figlet/program/unix/%{name}%{major}%{minor}.tar.gz	
Patch:		figlet-makefile.patch
URL:		http://st-www.cs.uiuc.edu/~chai/figlet.html
BuildRoot:	/tmp/%{name}-%{version}-buildroot

%description
Program for generating ASCII-art-like banners by using plenty of fonts. It
can be used for generating logos, e-mail signatures, etc.

%description -l pl
Program do generacji napisów ze znaków semigraficznych przy u¿yciu du¿ego
wyboru czcionek. Mo¿e byæ wykorzystany do tworzenia logo, podpisów do listów
e-mail, itp.

%prep
%setup -q -n %{name}%{major}%{minor}
%patch -p1

%build
CFLAGS="$RPM_OPT_FLAGS" \
make

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/usr/{games,share/games/figlet}
install -d $RPM_BUILD_ROOT/%{_mandir}/man6

install -s figlet $RPM_BUILD_ROOT/usr/games
install -s chkfont $RPM_BUILD_ROOT/usr/games
cp fonts/* $RPM_BUILD_ROOT/usr/share/games/figlet

gzip -9fn {FTP-NOTE,README,figfont.txt,figlist,figmagic,showfigfonts,figlet.6}
install figlet.6.gz $RPM_BUILD_ROOT/%{_mandir}/man6

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644, root, root, 755)
%attr(755, root, root) /usr/games/*
%doc {FTP-NOTE,README,figfont.txt,figlist,figmagic,showfigfonts}.gz

/usr/share/games/figlet
%{_mandir}/man6/figlet.6.gz

%changelog
* Thu Jun 10 1999 Micha³ Margula <alchemyx@pld.org.pl>
- initial rpm release
