%include	/usr/lib/rpm/macros.perl
%define	pdir	DBD
%define	pnam	Informix
Summary:	DBD::Informix perl module
Summary(pl):	Modu� perla DBD::Informix
Name:		perl-DBD-Informix
Version:	1.00.PC2
Release:	3
License:	GPL/Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	perl-DBI >= 1.13
BuildRequires:	rpm-perlprov >= 4.1-13
#BR: Informix ESQL/C 5.00 or later, or Client SDK 2.00 or later
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
IBM Informix Database Driver for Perl (previously known as
DBD::Informix) is the driver code that enables Perl 5.004 or 5.005 to
access Informix databases via the DBI module.

%description -l pl
IBM Informix Database Driver for Perl (poprzednio znany jako
DBD::Informix) jest sterownikiem pozwalaj�cym na dost�p do baz danych
Informix z poziomu Perla poprzez modu� DBI.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{?informixroot:INFORMIXDIR="%{informixroot}"; export INFORMIXDIR}
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor 

%{__make} OPTIMIZE="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%{__make} install DESTDIR=$RPM_BUILD_ROOT

install examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Announce ChangeLog README TODO
#%%{perl_vendorarch}/???
%{_mandir}/man3/*
%{_examplesdir}/%{name}-%{version}
