%define	snap	20010826
Summary:	icqlib library
Summary(pl):	Biblioteka icqlib
Name:		icqlib
Version:	1.2.0
Release:	0.%{snap}
License:	GPL
# snap from cvs repository
Group:		Libraries
Group(de):	Libraries
Group(es):	Bibliotecas
Group(fr):	Librairies
Group(pl):	Biblioteki
Group(pt_BR):	Bibliotecas
Group(ru):	‚…¬Ã…œ‘≈À…
Group(uk):	‚¶¬Ã¶œ‘≈À…
Source0:	http://download.sourceforge.net/%{name}/%{name}-%{version}-%{snap}.tar.gz
Patch0:		%{name}-m4.patch
URL:		http://kicq.sourceforge.net/icqlib.shtml
BuildRequires:	automake
BuildRequires:	autoconf
BuildRequires:	libtool
# right now conflicts because I don't know nothing about libicq
Conflicts:	libicq
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
icqlib is the most feature complete, open source, library
implementation of Mirabilis' ICQ protocol available on the Internet.
icqlib currently supports approximately 90% of the ICQ UDP v5 protocol
and 80% of the ICQ TCP v2 protocol, including new UIN registration,
chat, and file transfer.

%description -l pl
icqlib jest najbardziej kompletn±, open sourcow± bibliotek±
implementuj±c± protokÛ≥ Mirabilis ICQ. icqlib aktualnie obs≥uguj ok
90% protoko≥u ICQ UDP v5 oraz 80% ICQ TCP V2 w≥±czaj±c w to nowy
sposÛb rejstracji UIN, chat oraz transfer plikÛw.

%package devel
Summary:	Header files etc to develop icqlib applications
Summary(pl):	Pliki nag≥Ûwkowe i inne do icqlib
Group:		Development/Libraries
Group(de):	Entwicklung/Libraries
Group(es):	Desarrollo/Bibliotecas
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Group(pt_BR):	Desenvolvimento/Bibliotecas
Group(ru):	Ú¡⁄“¡¬œ‘À¡/‚…¬Ã…œ‘≈À…
Group(uk):	Úœ⁄“œ¬À¡/‚¶¬Ã¶œ‘≈À…
Requires:	%{name} = %{version}

%description devel
Header files etc you can use to develop icqlib applications.

%description -l pl devel
Pakiet ten zaziewra pliki nag≥Ûwkowe i inne do libicq niezbÍdne przy
tworzeniu aplikacji opartych o t± bibliotekÍ.

%package static
Summary:	Static icqlib libraries
Summary(pl):	Biblioteka statyczna icqlib
Group:		Development/Libraries
Group(de):	Entwicklung/Libraries
Group(es):	Desarrollo/Bibliotecas
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Group(pt_BR):	Desenvolvimento/Bibliotecas
Group(ru):	Ú¡⁄“¡¬œ‘À¡/‚…¬Ã…œ‘≈À…
Group(uk):	Úœ⁄“œ¬À¡/‚¶¬Ã¶œ‘≈À…
Requires:	%{name}-devel = %{version}

%description static
Static icqlib libraries.

%description -l pl static
Biblioteka statyczna icqlib.

%prep
%setup -q -n %{name}
%patch0 -p1

%build
%{__make} -f Makefile.cvs
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

gzip -9nf AUTHORS ChangeLog README TODO DEVEL CHANGES*

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc {AUTHORS,README,TODO}.gz
%attr(755,root,root) %{_libdir}/lib*.so.*.*

%files devel
%defattr(644,root,root,755)
%doc {ChangeLog,DEVEL,CHANGES*}.gz 
%attr(755,root,root) %{_libdir}/lib*.so
%attr(755,root,root) %{_libdir}/lib*.la
%{_includedir}/*.h

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
