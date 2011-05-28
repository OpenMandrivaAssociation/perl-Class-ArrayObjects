%define upstream_name    Class-ArrayObjects
%define upstream_version 1.03

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	%mkrel 2

Summary:	Class-ArrayObjects module for perl 
License:	GPL+ or Artistic
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Class/%{upstream_name}-%{upstream_version}.tar.bz2

BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}

%description
This module makes it easy to build classes using array based objects.
It's main goal is to allow one to create less memory hungry programs,
notably in memory-sensitive contexts such as mod_perl.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}
find . -type f -exec chmod 0644 {} \;

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make
make test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean 
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc Changes README
%{perl_vendorlib}/Class/ArrayObjects.pm
%{_mandir}/*/*
