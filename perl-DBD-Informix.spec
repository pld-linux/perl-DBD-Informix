#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	DBD
%define		pnam	Informix
Summary:	DBD::Informix - IBM Informix database driver for Perl
Summary(pl.UTF-8):   DBD::Informix - sterownik do bazy danych Informix IBM-a dla Perla
Name:		perl-DBD-Informix
Version:	2005.02
Release:	1
License:	GPL or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	31508761eac827fbfb1bdc878fe72702
BuildRequires:	perl-DBI >= 1.13
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	perl-ExtUtils-AutoInstall
#BR: Informix ESQL/C 5.00 or later, or Client SDK 2.00 or later
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
IBM Informix database driver for Perl (previously known as
DBD::Informix) is the driver code that enables Perl to access Informix
databases via the DBI module.

%description -l pl.UTF-8
Sterownik do bazy danych Informix IBM-a dla Perla (poprzednio znany
jako DBD::Informix) jest sterownikiem pozwalającym na dostęp do baz
danych Informix z poziomu Perla poprzez moduł DBI.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{?informixroot:INFORMIXDIR="%{informixroot}"; export INFORMIXDIR}
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make} \
	OPTIMIZE="%{rpmcflags}"

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Announce ChangeLog README TODO
#%%{perl_vendorarch}/???
%{_mandir}/man3/*
%{_examplesdir}/%{name}-%{version}
