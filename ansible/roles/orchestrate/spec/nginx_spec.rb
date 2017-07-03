
require 'spec_helper'


describe port(property['18080']) do
  it { should be_listening }
end

