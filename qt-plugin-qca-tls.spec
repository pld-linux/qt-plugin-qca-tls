%define		rname qca-tls
Summary:	Qt Cryptographic Architecture (QCA) SSL/TLS plugin
Summary(pl):	Wtyczka SSL/TLS dla Qt Cryptographic Architecture (QCA)
Name:		qt-plugin-qca-tls
Version:	20031209
Release:	0.1
License:	GPL v2
Group:		Libraries
Source0:	http://psi.affinix.com/beta/%{rname}-%{version}.tar.bz2
# Source0-md5:	4ae8b30955414acff9a1821e20098e6e
Patch0:		%{name}-install_path.patch
URL:		http://psi.affinix.com/
BuildRequires:	libstdc++-devel
BuildRequires:	openssl-devel >= 0.9.7c
BuildRequires:	qt-devel >= 3.1.2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_plugindir %{_libdir}/qt/plugins-mt/crypto

%description
A plugin to provide SSL/TLS capability to programs that utilize the Qt
Cryptographic Architecture (QCA).

%description -l pl
Wtyczka pozwalająca wykorzystać możliwości SSL/TLS w programach
korzystających z Qt Cryptographic Architecture (QCA).

%prep
%setup -qn %{rname}-%{version}
%patch0 -p1

%build
./configure \
	--qtdir="%{_prefix}"
	
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	INSTALL_ROOT=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%dir %{_plugindir}
%attr(755,root,root) %{_plugindir}/*.so
