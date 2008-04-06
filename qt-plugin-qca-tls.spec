%define		rname qca-tls
#
Summary:	Qt Cryptographic Architecture (QCA) SSL/TLS plugin
Summary(pl.UTF-8):	Wtyczka SSL/TLS dla Qt Cryptographic Architecture (QCA)
Name:		qt-plugin-%{rname}
Version:	1.0
Release:	8
Epoch:		1
License:	LGPL v2.1
Group:		Libraries
Source0:	http://delta.affinix.com/qca/%{rname}-1.0.tar.bz2
# Source0-md5:	886b1f60fc31de3b1a0bd93281e27b73
Patch0:		%{name}-openssl9x.patch
URL:		http://delta.affinix.com/qca/
BuildRequires:	libstdc++-devel
BuildRequires:	openssl-devel >= 0.9.7d
BuildRequires:	qmake
BuildRequires:	qt-devel >= 6:3.1.2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_plugindir %{_libdir}/qt/plugins-mt/crypto

%description
A plugin to provide SSL/TLS capability to programs that utilize the Qt
Cryptographic Architecture (QCA).

%description -l pl.UTF-8
Wtyczka pozwalająca wykorzystać możliwości SSL/TLS w programach
korzystających z Qt Cryptographic Architecture (QCA).

%prep
%setup -qn %{rname}-%{version}
%patch0 -p1

%build
export QTDIR=%{_prefix}
./configure

qmake %{rname}.pro \
	QMAKE_CXX="%{__cxx}" \
	QMAKE_LINK="%{__cxx}" \
	QMAKE_CXXFLAGS_RELEASE="%{rpmcflags}" \
	QMAKE_RPATH=

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
%attr(755,root,root) %{_plugindir}/*.so
