class TestapiController < ApplicationController
  
  def resetFixture
    User.delete_all
    
    if User.find(:all).empty?
      render :json => { 'errCode' => 1 }
    end
  end
  
  def unitTests
    render :json => { 'totalTests' => 0, 'nrFailed' => 10, 'output' => "Don't have any unit tests." }
  end
  
end
