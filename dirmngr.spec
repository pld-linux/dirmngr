Summary:	X509/LDAP certificate and revocation list client
Summary(pl.UTF-8):	Klient certyfikatów i list anulujących X509/LDAP
Name:		dirmngr
Version:	1.0.3
Release:	3
License:	GPL v2+
Group:		Applications
Source0:	ftp://ftp.gnupg.org/gcrypt/dirmngr/%{name}-%{version}.tar.bz2
# Source0-md5:	c1f2028d708e4d4ecbd6d6d647bd938b
Patch0:		%{name}-info.patch
URL:		http://www.gnupg.org/documentation/manuals/dirmngr/
BuildRequires:	automake
BuildRequires:	libassuan1-devel >= 1.0.5-2
BuildRequires:	libgcrypt-devel >= 1.4.0
BuildRequires:	libgpg-error-devel >= 1.4
BuildRequires:	libksba-devel >= 1.0.2
BuildRequires:	openldap-devel >= 2.4.6
BuildRequires:	pth-devel >= 1.3.7
BuildRequires:	texinfo
Requires:	libassuan1 >= 1.0.5-2
Requires:	libgcrypt >= 1.4.0
Requires:	libgpg-error >= 1.4
Requires:	libksba >= 1.0.2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
DirMngr is a client for managing and downloading certificate
revocation lists (CRLs) for X509 certificates and for downloading the
certificates themselves. DirMngr is usually invoked by gpgsm and in
general not used directly.

%description -l pl.UTF-8
DirMngr to klient do zarządzania i pobierania list anulujących
certyfikaty (CRLs - certificate revocation lists) dla certyfikatów
X509 oraz do pobierania samych certyfikatów. DirMngr jest zwykle
wywoływany przez gpgsm i nie używany bezpośrednio.

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

%{__rm} -r $RPM_BUILD_ROOT%{_docdir}/dirmngr
rm -f $RPM_BUILD_ROOT%{_infodir}/dir

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%postun	-p /sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc ChangeLog NEWS README*
%attr(755,root,root) %{_bindir}/dirmngr
%attr(755,root,root) %{_bindir}/dirmngr-client
%attr(755,root,root) %{_libexecdir}/dirmngr_ldap
%{_infodir}/dirmngr.info*
%{_mandir}/man1/dirmngr.1*
%{_mandir}/man1/dirmngr-client.1*
