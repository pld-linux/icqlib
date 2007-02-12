%define	snap	20010826
Summary:	icqlib library
Summary(pl.UTF-8):   Biblioteka icqlib
Name:		icqlib
Version:	1.2.0
Release:	0.%{snap}
License:	GPL
# snap from cvs repository
Group:		Libraries
Source0:	http://dl.sourceforge.net/icqlib/%{name}-%{version}-%{snap}.tar.gz
# Source0-md5:	69c009c91aaa7274862040950c339d5b
Patch0:		%{name}-m4.patch
URL:		http://kicq.sourceforge.net/icqlib.shtml
BuildRequires:	autoconf
BuildRequires:	automake
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

%description -l pl.UTF-8
icqlib jest najbardziej kompletną, open sourcową biblioteką
implementującą protokół Mirabilis ICQ. icqlib aktualnie obsługuj ok
90% protokołu ICQ UDP v5 oraz 80% ICQ TCP V2 włączając w to nowy
sposób rejestracji UIN, chat oraz transfer plików.

%package devel
Summary:	Header files etc to develop icqlib applications
Summary(pl.UTF-8):   Pliki nagłówkowe i inne do icqlib
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files etc you can use to develop icqlib applications.

%description devel -l pl.UTF-8
Pakiet ten zawiera pliki nagłówkowe i inne do libicq niezbędne przy
tworzeniu aplikacji opartych o tą bibliotekę.

%package static
Summary:	Static icqlib libraries
Summary(pl.UTF-8):   Biblioteka statyczna icqlib
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static icqlib libraries.

%description static -l pl.UTF-8
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

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS README TODO
%attr(755,root,root) %{_libdir}/lib*.so.*.*

%files devel
%defattr(644,root,root,755)
%doc ChangeLog DEVEL  CHANGES*
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/*.h

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
