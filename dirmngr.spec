Summary:	X509/LDAP certificate and revocation list client
Summary(pl):	Klient certyfikatów i list anuluj±cych X509/LDAP
Name:		dirmngr
Version:	0.4.5
Release:	1
License:	GPL
Group:		Applications
Source0:	ftp://ftp.gnupg.org/gcrypt/alpha/aegypten/%{name}-%{version}.tar.gz
# Source0-md5:	a6613347967f6679171c00808a17dfb2
Patch0:		%{name}-db4.patch
Patch1:		%{name}-info.patch
BuildRequires:	autoconf >= 2.52
BuildRequires:	automake
BuildRequires:	db-devel
BuildRequires:	libgcrypt-devel >= 1.1.5
BuildRequires:	libksba-devel
BuildRequires:	openldap-devel
BuildRequires:	texinfo
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
DirMngr is a client for managing and downloading certificate
revocation lists (CRLs) for X509 certificates and for downloading the
certificates themselves. DirMngr is usually invoked by gpgsm and in
general not used directly.

%description -l pl
DirMngr to klient do zarz±dzania i pobierania list anuluj±cych
certyfikaty (CRLs - certificate revocation lists) dla certyfikatów
X509 oraz do pobierania samych certyfikatów. DirMngr jest zwykle
wywo³ywany przez gpgsm i nie u¿ywany bezpo¶rednio.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir %{_infodir} >/dev/null 2>&1

%postun
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir %{_infodir} >/dev/null 2>&1

%files
%defattr(644,root,root,755)
%doc ChangeLog NEWS README*
%attr(755,root,root) %{_bindir}/dirmngr
%{_infodir}/dirmngr.info*
