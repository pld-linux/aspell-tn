Summary:	Tswana dictionary for aspell
Summary(pl):	S�ownik tswana dla aspella
Name:		aspell-tn
Version:	1.0.1
%define	subv	0
Release:	1
Epoch:		1
License:	GPL v2+
Group:		Applications/Text
Source0:	ftp://ftp.gnu.org/gnu/aspell/dict/tn/aspell5-tn-%{version}-%{subv}.tar.bz2
# Source0-md5:	6e5ef98452b36a211a4fc1fdbadda322
URL:		http://aspell.sourceforge.net/
BuildRequires:	aspell >= 0.50.0
Requires:	aspell >= 0.50.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Tswana dictionary (i.e. word list) for aspell.

%description -l pl
S�ownik tswana (lista s��w) dla aspella.

%prep
%setup -q -n %{name}-%{version}-%{subv}

%build
# note: configure is not autoconf-generated
./configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Copyright README
%{_libdir}/aspell/*
%{_datadir}/aspell/*