# NOTE: for dirmngr 2.x see gnupg2.spec
Summary:	X509/LDAP certificate and revocation list client
Summary(pl.UTF-8):	Klient certyfikatów i list anulujących X509/LDAP
Name:		dirmngr
Version:	1.1.1
Release:	5
License:	GPL v2+
Group:		Applications
Source0:	https://www.gnupg.org/ftp/gcrypt/dirmngr/%{name}-%{version}.tar.bz2
# Source0-md5:	f5a40e93bcf07a94522579bfd58a2c96
Patch0:		%{name}-info.patch
Patch1:		%{name}-am.patch
Patch2:		%{name}-pth.patch
Patch3:		%{name}-pl.po.patch
URL:		http://www.gnupg.org/documentation/manuals/dirmngr/
BuildRequires:	autoconf >= 2.59
BuildRequires:	automake >= 1:1.9.3
BuildRequires:	libassuan-devel >= 1:2.0.0
BuildRequires:	libgcrypt-devel >= 1.4.0
BuildRequires:	libgpg-error-devel >= 1.4
BuildRequires:	libksba-devel >= 1.0.2
BuildRequires:	openldap-devel >= 2.4.6
BuildRequires:	pth-devel >= 1.3.7
BuildRequires:	texinfo
Requires:	libassuan >= 1:2.0.0
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
%patch1 -p1
%patch2 -p0
%patch3 -p1

%{__rm} po/stamp-po

%build
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
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
%doc AUTHORS ChangeLog NEWS README THANKS TODO
%attr(755,root,root) %{_bindir}/dirmngr
%attr(755,root,root) %{_bindir}/dirmngr-client
%attr(755,root,root) %{_libexecdir}/dirmngr_ldap
%{_infodir}/dirmngr.info*
%{_mandir}/man1/dirmngr.1*
%{_mandir}/man1/dirmngr-client.1*
