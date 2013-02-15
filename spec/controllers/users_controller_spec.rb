require 'spec_helper'

describe UsersController do

  to "login" do
    usr = User.create(:user => "name", :password => "pass", :count => 1)
    
    usr.count.should be = 1
  end

end
