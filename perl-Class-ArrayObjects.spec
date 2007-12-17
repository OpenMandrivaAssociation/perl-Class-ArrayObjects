%define real_name Class-ArrayObjects

Summary:	Class-ArrayObjects module for perl 
Name:		perl-%{real_name}
Version:	1.02
Release:	%mkrel 2
License:	GPL or Artistic
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{real_name}
Source0:	%{real_name}-%{version}.tar.bz2
BuildRequires:	perl-devel
BuildArch:	noarch

%description
This module makes it easy to build classes using array based objects.
It's main goal is to allow one to create less memory hungry programs,
notably in memory-sensitive contexts such as mod_perl.

%prep
%setup -q -n %{real_name}-%{version} 
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


