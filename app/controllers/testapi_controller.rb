class TestapiController < ApplicationController
  
  def resetFixture
    User.delete_all
    
    if User.find(:all).empty?
      render :json => { 'errCode' => 1 }
    end
  end
  
  def unitTests
    
  end
  
end
