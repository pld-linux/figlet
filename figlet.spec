%define		major	2
%define		minor	2
%define		ver	1
Summary:	Awesome ASCII-art banners generator
Summary(pl.UTF-8):	Program do generowania odjazdowych napisów ASCII
Name:		figlet
Version:	%{major}.%{minor}.%{ver}
Release:	3
License:	Free
Group:		Applications/Games
Source0:	ftp://ftp.plig.org/pub/figlet/program/unix/%{name}%{major}%{minor}%{ver}.tar.gz
# Source0-md5:	216bc6d86952003cc3db75d5c36eb4f6
Patch0:		%{name}-makefile.patch
URL:		http://www.figlet.org/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Program for generating ASCII-art-like banners by using plenty of
fonts. It can be used for generating logos, e-mail signatures, etc.

%description -l pl.UTF-8
Program do generacji napisów ze znaków semigraficznych przy użyciu
dużego wyboru czcionek. Może być wykorzystany do tworzenia logo,
podpisów do listów e-mail, itp.

%prep
%setup -q -n %{name}%{major}%{minor}%{ver}
%patch0 -p1

%build
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags}" \
	DEFAULTFONTDIR=%{_datadir}/games/figlet

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_datadir}/games/figlet} \
	$RPM_BUILD_ROOT%{_mandir}/man6

install figlet chkfont $RPM_BUILD_ROOT%{_bindir}
install figlet.6 $RPM_BUILD_ROOT%{_mandir}/man6

cp -f fonts/* $RPM_BUILD_ROOT%{_datadir}/games/figlet

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%doc README  figfont.txt figlist figmagic showfigfonts
%{_datadir}/games/figlet
%{_mandir}/man6/figlet.6*
