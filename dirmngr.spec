Summary:	X509/LDAP certificate and revocation list client
Summary(pl):	Klient certyfikat�w i list anuluj�cych X509/LDAP
Name:		dirmngr
Version:	1.0.0
Release:	1
License:	GPL
Group:		Applications
Source0:	ftp://ftp.gnupg.org/gcrypt/dirmngr/%{name}-%{version}.tar.bz2
# Source0-md5:	59b263b33a59bfdb954d4a5cb001e5cc
Patch0:		%{name}-info.patch
BuildRequires:	automake
BuildRequires:	libassuan-devel >= 1:0.9.3
BuildRequires:	libgcrypt-devel >= 1.2.0
BuildRequires:	libgpg-error-devel >= 1.4
BuildRequires:	libksba-devel >= 1.0.0
BuildRequires:	openldap-devel >= 2.3.0
BuildRequires:	pth-devel >= 1.3.7
BuildRequires:	texinfo
Requires:	libassuan >= 1:0.9.3
Requires:	libgcrypt >= 1.2.0
Requires:	libgpg-error >= 1.4
Requires:	libksba >= 1.0.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
DirMngr is a client for managing and downloading certificate
revocation lists (CRLs) for X509 certificates and for downloading the
certificates themselves. DirMngr is usually invoked by gpgsm and in
general not used directly.

%description -l pl
DirMngr to klient do zarz�dzania i pobierania list anuluj�cych
certyfikaty (CRLs - certificate revocation lists) dla certyfikat�w
X509 oraz do pobierania samych certyfikat�w. DirMngr jest zwykle
wywo�ywany przez gpgsm i nie u�ywany bezpo�rednio.

%prep
%setup -q
%patch0 -p1

%build
cp -f /usr/share/automake/config.* .
%configure \
	--with-ldap=/usr
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
%attr(755,root,root) %{_bindir}/dirmngr-client
%attr(755,root,root) %{_libexecdir}/dirmngr_ldap
%{_infodir}/dirmngr.info*
%{_mandir}/man1/dirmngr.1*
%{_mandir}/man1/dirmngr-client.1*
