class UsersController < ApplicationController
  
  SUCCESS = 1
  ERR_BAD_CREDENTIALS = -1
  ERR_USER_EXISTS = -2
  ERR_BAD_USERNAME = -3
  ERR_BAD_PASSWORD = -4
  
  def login
    @user = User.find_by_user(params[:user])
    if @user
      if @user.password == params[:password]
        @count = @user.count + 1
        @user.update_attribute :count, @count
        render :json => { 'errCode' => SUCCESS, 'count' => @user.count }
      else
        render :json => { 'errCode' => ERR_BAD_CREDENTIALS }
      end
    else
      render :json => { 'errCode' => ERR_BAD_CREDENTIALS }
    end
  end
  
  
  def add
    @username = params[:user]
    @pass = params[:password]
    
    if User.find_by_user(@username)
      render :json => { 'errCode' => ERR_USER_EXISTS } 
    elsif @username.length > 128 || @username.empty?
      render :json => { 'errCode' => ERR_BAD_USERNAME }
    elsif @pass.length > 128
      render :json => { 'errCode' => ERR_BAD_PASSWORD }
    else
      @user = User.create(:user => @username, :password => @pass, :count => 1)
      render :json => { 'errCode' => SUCCESS, 'count' => @user.count }
    end
  end
  
end
