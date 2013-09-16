### RPM external pythia8 175

Requires: hepmc

Source: http://cern.ch/service-spi/external/MCGenerators/distribution/%{n}/%{n}-%{realversion}-src.tgz
%prep
%setup -q -n %{n}/%{realversion}

export HEPMCLOCATION=${HEPMC_ROOT} 
export HEPMCVERSION=${HEPMC_VERSION} 
./configure --enable-shared --with-hepmc=${HEPMC_ROOT}

%build
make 

%install
tar -c lib include xmldoc | tar -x -C %i
