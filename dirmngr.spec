Summary:	X509/LDAP certificate and revocation list client
Summary(pl):	Klient certyfikatów i list anuluj±cych X509/LDAP
Name:		dirmngr
Version:	0.5.3
Release:	1
License:	GPL
Group:		Applications
Source0:	ftp://ftp.gnupg.org/gcrypt/alpha/dirmngr/%{name}-%{version}.tar.gz
# Source0-md5:	05ba1c4eb6f50f8a053ce67253becc1b
Patch0:		%{name}-info.patch
BuildRequires:	automake
BuildRequires:	libassuan-devel >= 1:0.6.2
BuildRequires:	libgcrypt-devel >= 1.1.94
BuildRequires:	libgpg-error >= 0.7
BuildRequires:	libksba-devel >= 0.9.5
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

%build
cp -f /usr/share/automake/config.* .
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir %{_infodir} >/dev/null 2>&1

%postun
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir %{_infodir} >/dev/null 2>&1

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc ChangeLog NEWS README*
%attr(755,root,root) %{_bindir}/dirmngr
%{_infodir}/dirmngr.info*
