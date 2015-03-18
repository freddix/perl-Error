%include	/usr/lib/rpm/macros.perl

Summary:	Error - error/exception handling in an OO-ish way
Name:		perl-Error
Version:	0.17023
Release:	1
# same as perl
License:	GPL v1 or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Error/Error-%{version}.tar.gz
# Source0-md5:	98524ffbd268013e00697a5826a83d37
BuildRequires:	perl-devel
BuildRequires:	rpm-perlprov
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Error Perl module provides two interfaces. Firstly Error provides
a procedural interface to exception handling. Secondly Error is a base
class for errors/exceptions that can either be thrown, for subsequent
catch, or can simply be recorded.

%prep
%setup -q -n Error-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}
%{__make} test

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README
%{perl_vendorlib}/Error.pm
%dir %{perl_vendorlib}/Error
%{perl_vendorlib}/Error/Simple.pm
%{_mandir}/man3/*

